import os

############################
# General Settings         #
############################
DEBUG = False
STREAM_ENGINE_VERSION = "1.0.3"
# Cassandra process pool size
POOL_SIZE = 4
LOGGING_CONFIG = 'logging.conf'
REQUEST_TIMEOUT_SECONDS = 3600  # 60 minutes
# Maximum depth difference between two instruments to be considered "near"
MAX_DEPTH_VARIANCE = 20
METADATA_CACHE_SECONDS = 600
PARAMETER_LOGGING = '/opendap_export/stream_engine'
DPA_VERSION_VARIABLE = "version"
INTERNAL_OUTPUT_EXCLUDE_LIST = ['bin', ]
CONFIG_DIR = os.path.dirname(__file__)
ASYNC_DOWNLOAD_BASE_DIR = '/opt/ooi/async'


############################
# SAN (MTA) Settings       #
############################
SAN_BASE_DIRECTORY = '/opt/ooi/SAN/'
# When loading data back into cassandra should we allow writing to an already present databin.
SAN_CASS_OVERWRITE = True
# 'san' or 'cass': If data is present in a time bin on both the SAN and Cassandra this option chooses
# which value to take if the number of entries match.  Otherwise the location with the most data is chosen.
PREFERRED_DATA_LOCATION = 'cass'
# The name of the variable that contains the version string for the ion_functions at the package level.


############################
# Cassandra Settings       #
############################
CASSANDRA_CONTACT_POINTS = ['127.0.0.1']
CASSANDRA_KEYSPACE = 'ooi'
CASSANDRA_CONNECT_TIMEOUT = 60
CASSANDRA_FETCH_SIZE = 1000
CASSANDRA_DEFAULT_TIMEOUT = 60
CASSANDRA_QUERY_CONSISTENCY = 'LOCAL_QUORUM'


############################
# UFrame Settings          #
############################
ANNOTATION_HOST = 'localhost'
ASSET_HOST = 'localhost'
STREAM_METADATA_SERVICE_URL = 'http://127.0.0.1:12571/streamMetadata'
PARTITION_METADATA_SERVICE_URL = 'http://127.0.0.1:12571/partitionMetadata'


############################
# NetCDF Settings          #
############################
NETCDF_TITLE = "Data produced by Stream Engine version {:s}".format(STREAM_ENGINE_VERSION)
NETCDF_INSTITUTION = "Ocean Observatories Initiative"
NETCDF_HISTORY_COMMENT = "generated from Stream Engine"
NETCDF_REFERENCE = "More information can be found at http://oceanobservatories.org/"
NETCDF_COMMENT = ""
NETCDF_CONVENTIONS = "CF-1.6"
NETCDF_METADATA_CONVENTIONS = "Unidata Dataset Discovery v1.0"
NETCDF_FEATURE_TYPE = "point"
NETCDF_CDM_DATA_TYPE = "Point"
NETCDF_NODC_TEMPLATE_VERSION = "NODC_NetCDF_TimeSeries_Orthogonal_Template_v1.1"
NETCDF_STANDARD_NAME_VOCABULARY = "NetCDF Climate and Forecast (CF) Metadata Convention Standard Name Table 29"
NETCDF_SUMMARY = "Dataset Generated by Stream Engine from Ocean Observatories Initiative"
NETCDF_NAMING_AUTHORITY = "org.oceanobservatories"
NETCDF_CREATOR_NAME = "Ocean Observatories Initiative"
NETCDF_CREATOR_URL = "http://oceanobservatories.org/"
NETCDF_CREATOR_EMAIL = ""
NETCDF_PROJECT = "Ocean Observatories Initiative"
NETCDF_PROCESSING_LEVEL = "L2"
NETCDF_KEYWORDS_VOCABULARY = ""
NETCDF_KEYWORDS = ""
NETCDF_ACKNOWLEDGEMENT = ""
NETCDF_CONTRIBUTOR_NAME = ""
NETCDF_CONTRIBUTOR_ROLE = ""
NETCDF_PUBLISHER_NAME = "Ocean Observatories Initiative"
NETCDF_PUBLISHER_URL = "http://oceanobservatories.org/"
NETCDF_INFO_URL = "http://oceanobservatories.org/"
NETCDF_SOURCE_URL = "http://oceanobservatories.org/"
NETCDF_PUBLISHER_EMAIL = ""
NETCDF_LICENSE = ""
NETCDF_CALENDAR_TYPE = "gregorian"
NETCDF_UNLIMITED_DIMS = ['obs']
NETCDF_CHUNKSIZES = 10000

Z_AXIS_NAME = "depth"
Z_POSITIVE = "down"
Z_DEFAULT_UNITS = 'meters'
Z_LONG_NAME = 'Deployment depth of sensor below sea surface'
Z_STANDARD_NAME = 'depth'
Z_RESOLUTION = 0.1
GEOSPATIAL_LAT_LON_RES = 0.1

# HDF5 Compression 0 = None, compression level 1 to 5
HDF5_COMP_LEVEL = 1

INTERNAL_OUTPUT_MAPPING = {
    'deployment': 'int32',
    'id': 'str',
    'lat': 'float64',
    'lon': 'float64'
}

# Added these for netcdf outputs because the values in preload are not as reliable
# as they should be and we would like to filter purely based on data type.
FILL_VALUES = {
    "float16": float('nan'),
    "float32": float('nan'),
    "float64": float('nan'),
    "int": -9999999,
    "int8": -9,
    "int16": -9999,
    "int32": -9999999,
    "int64": -9999999,
    "uint8": 0xff,
    "uint16": 0xffff,
    "uint32": 0xffffffff,
    "uint64": 0xffffffffffffffff,
    "string": "",
    "boolean": -9
}

# Used for fill values when location data is missing
LAT_FILL = 90.0
LON_FILL = -180.0
DEPTH_FILL = 0.0


############################
# Estimation Settings      #
############################
SIZE_CONFIG = os.path.join(CONFIG_DIR, 'stream_nc_sizes.cfg')
# default bytes/particle estimate (for a NetCDF file)
PARTICLE_DENSITY = 1000
SECONDS_PER_BYTE = 0.0000041


############################
# Aggregation Settings     #
############################
# Turn netcdf aggregation on or off
AGGREGATE = True
# Directory to place intermediate netcdf results
LOCAL_ASYNC_DIR = '/local/async_results'
# Directory to place aggregated netcdf results
FINAL_ASYNC_DIR = '/opt/ooi/async'
# Names of other stream engine nodes for aggregation
# This should match the output of 'uname -n' to allow this node to skip itself
STREAM_ENGINE_NODES = []
# Maximum number of concurrent rsync subprocesses
MAX_RSYNC_WORKERS = 4
# Maximum number of rsync retries
MAX_RETRY_COUNT = 3
# Maximum single file size for aggregation, in Bytes
MAX_AGGREGATION_SIZE = 500e6
# Maximum time spent in aggregation, in seconds
AGGREGATION_TIMEOUT_SECONDS = 7200


############################
# Query Settings           #
############################
COLLAPSE_TIMES = True
# If the ratio of total data to requested points is less than this value all of the data is returned
UI_FULL_RETURN_RATIO = 2.0
# If the ratio of total data to requested points is less than this value all and the total data in
# Cassandra is less than the full sample limit a linear sample from all of the data is returned
UI_FULL_SAMPLE_RATIO = 5.0
# If the ratio of total data to requested points is less than the UI_FULL_SAMPLE_RATIO and
# the total number of data points is less than this value a linear sampling of all of the data is returned
# Otherwise a sampling method is used pre query.
UI_FULL_SAMPLE_LIMIT = 5000
# set a hard limit for the maximum size a limited query can be.  All data can be accessed using an async query.
UI_HARD_LIMIT = 20000
QC_RESULTS_STORAGE_SYSTEM = 'none'  # 'log' to write qc results to a file, 'cass' to write qc results to a database
# Number of cassandra rows used to the correct deployment for padding of streams which provide
# cal coefficients and other needed data
LOOKBACK_QUERY_LIMIT = 100
MAX_BIN_SIZE_MIN = 20160
# Where to start unbounded queries 2010-01-01T00:00:00.000Z
UNBOUND_QUERY_START = 3471292800


############################
# X/Y/Z Interp. Settings   #
############################
PRESSURE_DPI = 'PRESWAT_L1'
GPS_STREAM_ID = 761
LATITUDE_PARAM_ID = 1335
LONGITUDE_PARAM_ID = 1336
INT_PRESSURE_NAME = 'int_ctd_pressure'
