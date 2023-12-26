DRF_API_LOGGER_DATABASE = True
DRF_API_LOGGER_SIGNAL = True
DRF_LOGGER_QUEUE_MAX_SIZE = 50
DRF_LOGGER_INTERVAL = 10
# DRF_API_LOGGER_SKIP_NAMESPACE = ['APP_NAMESPACE1', 'APP_NAMESPACE2']
# DRF_API_LOGGER_SKIP_URL_NAME = ['url_name1', 'url_name2']
DRF_API_LOGGER_EXCLUDE_KEYS = ['password', 'token', 'access',
                               'refresh', 'bearer', 'Bearer']  # Sensitive data will be replaced with "***FILTERED***".
# DRF_API_LOGGER_DEFAULT_DATABASE = 'default'  # Default to "default" if not specified
# DRF_API_LOGGER_SLOW_API_ABOVE = 200  # Default to None. Specify in milliseconds.
DRF_API_LOGGER_METHODS = ['GET']  # Default to empty list (Log all the requests).
# DRF_API_LOGGER_METHODS = ['GET', 'POST', 'DELETE', 'PUT']  # Default to empty list (Log all the requests).
# DRF_API_LOGGER_STATUS_CODES = [200, 400, 404, 500]  # Default to empty list (Log all responses).
DRF_API_LOGGER_STATUS_CODES = [200]  # Default to empty list (Log all responses).
DRF_API_LOGGER_TIMEDELTA = 120 # UTC + 120 Minutes = IST (2:Hours, 00:Minutes ahead from UTC)
# Specify in minutes.
# DRF_API_LOGGER_MAX_REQUEST_BODY_SIZE = 1024  # default to -1, no limit.
# DRF_API_LOGGER_MAX_RESPONSE_BODY_SIZE = 1024  # default to -1, no limit.
DRF_API_LOGGER_PATH_TYPE = 'ABSOLUTE'  # Default to ABSOLUTE if not specified
# Possible values are ABSOLUTE, FULL_PATH or RAW_URI
DRF_API_LOGGER_ENABLE_TRACING = True  # default to False
# DRF_API_LOGGER_TRACING_FUNC = 'foo.bar.func_name'
# DRF_API_LOGGER_TRACING_ID_HEADER_NAME: str = 'X_TRACING_ID'  # Replace with actual header name.
