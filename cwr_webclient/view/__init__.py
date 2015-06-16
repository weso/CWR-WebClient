__author__ = 'Bernardo'

from cwr_webclient.view.common.routes import common_blueprint
from cwr_webclient.view.cwr.contents.routes import cwr_contents_blueprint
from cwr_webclient.view.cwr.acknowledgement.routes import \
    cwr_acknowledgement_blueprint
from cwr_webclient.view.cwr.match.routes import cwr_match_blueprint
from cwr_webclient.view.cwr.file.routes import cwr_file_blueprint
from cwr_webclient.view.cwr.upload.routes import cwr_upload_blueprint
from cwr_webclient.view.mera.match.routes import mera_match_blueprint
from cwr_webclient.view.uso.upload.routes import uso_upload_blueprint
