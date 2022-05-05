LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'filters': {
    'require_debug_false': {
        '()': 'django.utils.log.RequireDebugFalse',
    },
    'require_debug_true': {
        '()': 'django.utils.log.RequireDebugTrue',
    },
},
'formatters': {
    'django.server': {
        '()': 'django.utils.log.ServerFormatter',
        'format': '[%(server_time)s] [%(levelname)s] %(message)s',
    },
    'root': {
        '()': 'django.utils.log.ServerFormatter',
        'format': '[%(asctime)s] [%(process)d] [%(levelname)s] %(name)s %(message)s',
    }
},
'handlers': {
    'console': {
        'level': 'INFO',
        'filters': ['require_debug_true'],
        'class': 'logging.StreamHandler',
        'formatter': 'root'
    },
    'console_on_not_debug': {
        'level': 'INFO',
        'filters': ['require_debug_false'],
        'class': 'logging.StreamHandler',
    },
    'django.server': {
        'level': 'INFO',
        'class': 'logging.StreamHandler',
        'formatter': 'django.server',
    },
    'file_on_not_debug': {
        'level': 'INFO',
        'class': 'logging.FileHandler',
        'filters': ['require_debug_false'],
        'filename': 'logs/gunicorn.log',
        'formatter': 'root',
    },
    'file': {
        'level': 'DEBUG',
        'class': 'logging.FileHandler',
        'filters': ['require_debug_true'],
        'filename': 'logs/gunicorn.debug.log',
        'formatter': 'root',
    },
},
'loggers': {
    '': {
        'handlers': ['console', 'file', 'console_on_not_debug', 'file_on_not_debug'],
        'level': 'INFO',
    },
    'django.server': {
        'handlers': ['django.server'],
        'level': 'INFO',
        'propagate': False,
    },
}
}