__author__ = 'Bernardo'

from cwr_webclient.view.common.routes import common_blueprint
from cwr_webclient.view.cwr.validation.routes import cwr_validation_blueprint
from cwr_webclient.view.cwr.acknowledgement.routes import cwr_acknowledgement_blueprint
from cwr_webclient.view.cwr.match.routes import cwr_match_blueprint
from cwr_webclient.view.cwr.file.routes import cwr_file_blueprint
from cwr_webclient.view.cwr.workload.routes import cwr_workload_blueprint
from cwr_webclient.view.cwr.database.routes import cwr_database_blueprint
