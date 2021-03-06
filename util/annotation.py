import os
import json
import logging
from collections import namedtuple

import datetime
import ntplib
import numpy as np
import requests

from engine import app
from util.jsonresponse import NumpyJSONEncoder
from util.common import WriteErrorException

log = logging.getLogger(__name__)

# Seconds from NTP epoch to UNIX epoch
NTP_OFFSET_SECS = 2208988800


class AnnotationServiceInterface(object):
    def __init__(self, anno_host, port=12580):
        self.base_url = 'http://%s:%d/anno/find' % (anno_host, port)

    def find_annotations(self, key, time_range):
        start, stop = time_range.as_millis()
        params = {
            'refdes': key.as_three_part_refdes(),
            'method': key.method,
            'stream': key.stream_name,
            'beginDT': start,
            'endDT': stop
        }

        response = requests.get(self.base_url, params=params)
        payload = response.json()

        if response.status_code == 200:
            result = []
            for record in payload:
                if record.pop('@class', None) == '.AnnotationRecord':
                    annotation_record = AnnotationRecord(**record)
                    if annotation_record.stop:
                        # only store bounded annotations, skip open ended annotations
                        # leave open ended annotation support for future enhacement work
                        result.append(annotation_record)
            return result

        else:
            log.error('Error fetching annotations: <%r> %r', response.status_code, payload)
            return []


class AnnotationRecord(object):
    def __init__(self, id=None, subsite=None, node=None, sensor=None, method=None, stream=None, annotation=None,
                 exclusionFlag=None, beginDT=None, endDT=None, source=None, qcFlag=None, parameters=None, **kwargs):
        self.id = id
        self.subsite = subsite
        self.node = node
        self.sensor = sensor
        self.method = method
        self.stream = stream
        self.annotation = annotation
        self.exclusion_flag = exclusionFlag
        self.source = source
        self.qc_flag = qcFlag
        self.parameters = parameters

        self._start_millis = beginDT
        self._stop_millis = endDT
        self._start_ntp = ntplib.system_to_ntp_time(self._start_millis / 1000.0)
        self._stop_ntp = ntplib.system_to_ntp_time(self._stop_millis / 1000.0) if self._stop_millis else None
        self.start = datetime.datetime.utcfromtimestamp(self._start_millis / 1000.0)
        self.stop = datetime.datetime.utcfromtimestamp(self._stop_millis / 1000.0) if self._stop_millis else None

    def as_dict(self):
        return {k: v for k, v in self.__dict__.iteritems() if not k.startswith('_')}


class AnnotationStore(object):
    """
    Handles the storage of annotations during the lifecycle of a request.
    """

    def __init__(self):
        self._store = []
        self._ntpstart = None
        self._ntpstop = None

    def add_annotations(self, annotations):
        self._store.extend(annotations)

    def query_annotations(self, stream_key, time_range):
        self._store = _service.find_annotations(stream_key, time_range)

    def get_annotations(self):
        return list(self._store)

    def as_dict_list(self):
        return [x.as_dict() for x in self._store]
    
    def dump_json(self, filepath):
        try:
            parent_dir = os.path.dirname(filepath)
            if not os.path.exists(parent_dir):
                try:
                    os.makedirs(parent_dir)
                except OSError:
                    if not os.path.isdir(parent_dir):
                        raise WriteErrorException('Unable to create local output directory: %s' % parent_dir)
            with open(filepath, 'a') as fh:
                annotations = {'annotations': self.as_dict_list()}
                json.dump(annotations, fh, indent=2, separators=(',', ': '), cls=NumpyJSONEncoder)
        except EnvironmentError as e:
            log.error('Failed to write annotation file: %s', e)

    @staticmethod
    def _update_mask(times, mask, anno):
        return mask & ((times < anno._start_ntp) | (times > anno._stop_ntp))

    def get_exclusion_mask(self, times):
        mask = np.ones_like(times).astype('bool')
        for anno in self._store:
            if anno.exclusion_flag:
                mask = self._update_mask(times, mask, anno)

        return mask

    def has_exclusion(self):
        return any((x.exclusion_flag for x in self._store))


_service = AnnotationServiceInterface(app.config.get('ANNOTATION_HOST'))
