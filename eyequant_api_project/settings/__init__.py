import os

if os.environ.get('PROD'):
    from .production import *
else:
    from .development import *
