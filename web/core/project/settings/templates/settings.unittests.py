# mypy: ignore-errors

DEBUG = True

MIDDLEWARE += ('web.core.common.middleware.LoggingMiddleware',)
LOGGING['formatters']['colored'] = {
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['core']['level'] = 'DEBUG'
LOGGING['handlers']['console']['level'] = 'DEBUG'
LOGGING['handlers']['console']['formatter'] = 'colored'
