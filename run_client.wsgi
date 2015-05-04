#!/usr/bin/python
import sys
import logging
from cwr_webclient import create_app
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0,"/var/www/cwr/")
#os.chdir("/var/www/cwr")

application = create_app()