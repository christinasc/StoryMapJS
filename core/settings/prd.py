"""
Production settings and globals.
"""
import sys
import os
from .base import *

# Import secrets
secrets_path = os.path.normpath(os.path.join(PROJECT_ROOT, '../secrets/storymap/prd'))
sys.path.append(secrets_path)

from secrets import *

# Set Flask configuration
os.environ['FLASK_CONFIG_MODULE'] = os.path.join(secrets_path, 'flask_config.py')

STATIC_URL = 'http://media.knightlab.com/storymap/'

CDN_URL = 'http://cdn.knightlab.com/libs/storymap/latest/'

DATABASES = {
    'default': {
        'ENGINE': 'mongo',
        'NAME': 'storymap',
        'HOST': 'prd-mongo1.knilab.com',
        'PORT': 27017,
    }
}

# name of user storage bucket on S3
AWS_STORAGE_BUCKET_NAME = 'uploads.knightlab.com'

# User storage bucket url on S3
AWS_STORAGE_BUCKET_URL = '//s3.amazonaws.com/uploads.knightlab.com/'