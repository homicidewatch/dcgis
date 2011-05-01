from settings import *

from bundle_config import config

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "HOST": config['postgres']['host'],
        "PORT": int(config['postgres']['port']),
        "USER": config['postgres']['username'],
        "PASSWORD": config['postgres']['password'],
        "NAME": config['postgres']['database'],
    },
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '%s:%s' % (config['redis']['host'], config['redis']['port']),
        'OPTIONS': {
            'PASSWORD': config['redis']['password'],
        },
    },
}
