from entity.config.database_config import DataBaseConfig
from utils.logger_util import LoggerUtil
import yaml

class ConfigLoader():

    @classmethod
    def load_config(self, configPath) :
        configInfo = open(configPath, 'r', encoding='utf-8').read()
        configInfoDict = yaml.load(configInfo, Loader=yaml.FullLoader)
        logger = LoggerUtil().getLogger("database-backup")
        logger.info("load application file success!")
        logger.info(configInfoDict)
        return DataBaseConfig(
            configInfoDict.get("database").get("application").get("name"),
            configInfoDict.get("database").get("type"),
            configInfoDict.get("database").get("url"),
            configInfoDict.get("database").get("port"),
            configInfoDict.get("database").get("username"),
            configInfoDict.get("database").get("password"),
            configInfoDict.get("database").get("databaseName"),
            configInfoDict.get("database").get("charset"),
            configInfoDict.get("database").get("backMax"),
            configInfoDict.get("database").get("regEx"),
            configInfoDict.get("database").get("cron")
            )