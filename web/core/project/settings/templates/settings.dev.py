# mypy: ignore-errors

DEBUG = True

SECRET_KEY = 'django-insecure-4wmwf@=$xbi#0=z=d#0gb2w367q35vik56=d8+66ip=*%b1$o='

MIDDLEWARE += ('web.core.common.middleware.LoggingMiddleware',)
LOGGING['formatters']['colored'] = {
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['core']['level'] = 'DEBUG'
LOGGING['handlers']['console']['level'] = 'DEBUG'
LOGGING['handlers']['console']['formatter'] = 'colored'
