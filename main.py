from entity.config.database_config import DataBaseConfig
from utils.logger_util import LoggerUtil
from handler.handler import Handler
import os

currentPath = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(currentPath, "application.yml")
logger = LoggerUtil().getLogger("database-backup")
logger.info(open(currentPath + "/.github/logo.txt").read())
logger.info("application start……")

Handler().create_task(DataBaseConfig(configPath))
logger.info("application success")