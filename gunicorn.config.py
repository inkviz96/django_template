import multiprocessing

#######################################################
# Change only loglevel                                #
#######################################################
accesslog = '-'
errorlog = '-'
loglevel = "info"
capture_output = True
enable_stdio_inheritance = True
#######################################################

#######################################################
# Don't touch. This important for prevent DDOS attack #
#######################################################
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190
forwarded_allow_ips = '127.0.0.1' # Change for production to frontend server
#######################################################

max_requests = 500
max_requests_jitter = 20
workers = multiprocessing.cpu_count() * 2 + 1
