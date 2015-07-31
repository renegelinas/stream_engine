DEBUG = False

CASSANDRA_CONTACT_POINTS = ['127.0.0.1']
CASSANDRA_KEYSPACE = 'ooi'
CASSANDRA_CONNECT_TIMEOUT = 60
CASSANDRA_FETCH_SIZE = 1000
CASSANDRA_DEFAULT_TIMEOUT = 60
CASSANDRA_QUERY_CONSISTENCY = 'QUORUM'

SAN_BASE_DIRECTORY = '/opt/ooi/SAN/'
ANNOTATION_URL = 'http://localhost:12580/annotations/find/'

POOL_SIZE = 4

LOGGING_CONFIG='logging.conf'

NETCDF_TITLE = "Data produced by Stream Engine version 0.6"
NETCDF_INSTITUTION = "Ocean Observatories Initiative"
NETCDF_HISTORY_COMMENT = "generated from Stream Engine"
NETCDF_REFERENCE = "More information can be found at http://oceanobservatories.org/"
NETCDF_COMMENT = ""

