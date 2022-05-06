LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "root": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[%(asctime)s] [%(process)d] [%(levelname)s] %(name)s %(message)s",
        },
        "file_format": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[%(asctime)s] [%(levelname)s] [%(module)s:%(funcName)s(%(lineno)d)] %(name)s: %(message)s | %(request)s [%(status_code)d]",
        },
        "django.db.backends": {
            "format": "[%(asctime)s] [%(levelname)s] duration:[%(duration)s] | %(sql)s | params:(%(params)s)"
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "root",
        },
        "console_on_not_debug": {
            "level": "INFO",
            "filters": ["require_debug_false"],
            "class": "logging.StreamHandler",
        },
        "file_on_not_debug": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filters": ["require_debug_false"],
            "filename": "logs/gunicorn.log",
            "formatter": "file_format",
            "backupCount": 10,
            "maxBytes": 104857600,
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filters": ["require_debug_true"],
            "filename": "logs/gunicorn.debug.log",
            "formatter": "file_format",
            "backupCount": 5,
            "maxBytes": 52428800,
        },
        "django.db.backends": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filters": ["require_debug_true"],
            "filename": "logs/sql.log",
            "formatter": "django.db.backends",
            "backupCount": 5,
            "maxBytes": 52428800,
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "console_on_not_debug"],
            "level": "INFO",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["file", "file_on_not_debug"],
            "level": "INFO",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["django.db.backends"],
            "level": "DEBUG",
        },
    },
}
