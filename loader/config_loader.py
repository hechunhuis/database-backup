from entity.config.database_config import DataBaseConfig
import yaml

class ConfigLoader():

    @classmethod
    def load_config(self, configPath) :
        configInfo = open(configPath, 'r', encoding='utf-8').read()
        configInfoDict = yaml.load(configInfo, Loader=yaml.FullLoader)
        
        return DataBaseConfig(configInfoDict.get("database").get("type"),
                              configInfoDict.get("database").get("url"),
                              configInfoDict.get("database").get("port"),
                              configInfoDict.get("database").get("username"),
                              configInfoDict.get("database").get("password"),
                              configInfoDict.get("database").get("databaseName"),
                              configInfoDict.get("database").get("savePath"),
                              configInfoDict.get("database").get("backMax"),
                              configInfoDict.get("database").get("regEx"),
                              configInfoDict.get("database").get("cron"))