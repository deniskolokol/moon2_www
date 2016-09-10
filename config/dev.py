from config.common import *

try:
    from config.local import *
except ImportError:
    print 'Local settings not found, running on common.'
