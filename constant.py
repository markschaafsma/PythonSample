'''
Purpose:

    This module defines constants that are used though out the Claims Reporting application.

Revision History:

    16/11/2020   Mark Schaafsma   Added LOG_LEVELs.
    29/10/2020   Mark Schaafsma   Added MANY_UPDATE_TYPE and DT (date) constants.
    28/09/2020   Mark Schaafsma   Created. 

'''


PRD_ENV = 'PRD'
UAT_ENV = 'UAT'
DEV_ENV = 'DEV'
LOC_ENV = 'LOCAL'


API_JOB_TYPE = 'API'
CSV_JOB_TYPE = 'CSV'


JSON_RUN_TYPE = 'JSON'
INSERT_RUN_TYPE = 'INSERT'
INSERT_AND_UPDATE_RUN_TYPE = 'INSERT-AND-UPDATE'


BULK_UPDATE_TYPE = 'BULK'
MANY_UPDATE_TYPE = 'MANY'
SINGLE_UPDATE_TYPE = 'SINGLE'


TRUE_KEEP_RESPONSE = 'TRUE'
FALSE_KEEP_RESPONSE = 'FALSE'


LOG_LEVEL_DEBUG = 'DEBUG'
LOG_LEVEL_INFO = 'INFO'
LOG_LEVEL_WARNING = 'WARNING'
LOG_LEVEL_ERROR = 'ERROR'
LOG_LEVEL_CRITICAL = 'CRITICAL'


DT_AWARE_OBJECT = 1
DT_NAIVE_OBJECT = 2
DT_AWARE_STRING = 3
DT_NAIVE_STRING = 4