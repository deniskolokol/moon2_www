try:
    from config.local import *
except ImportError:
    print 'Local settings not found, running on common.'

# config.local imports config.base and adds necessary settings.
# Overrides follow:
DEBUG = False
