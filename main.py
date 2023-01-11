from loader.environment_loader import EnvironmentLoader
from loader.config_loader import ConfigLoader
from utils.logger_util import LoggerUtil
from handler.handler import Handler
import os

logger = LoggerUtil().getLogger("database-backup")
logger.info("application start……")
configName = "application.yml"
currentPath = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(currentPath, configName)

database_config = ConfigLoader().load_config(configPath)
database_config = EnvironmentLoader().load_config(database_config)
Handler().create_task(database_config)
logger.info("application success")