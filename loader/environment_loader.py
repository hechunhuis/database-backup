import os
from entity.config.database_config import DataBaseConfig

class EnvironmentLoader() :
    '''
    环境加载器
    '''
    def load_config(self, database_config:DataBaseConfig) -> None:
        '''
        加载配置信息
        '''
        _type = os.getenv("database.type")
        _url = os.getenv("database.url")
        _port = os.getenv("database.port")
        _username = os.getenv("database.username")
        _password = os.getenv("database.password")
        _database_name = os.getenv("database.databaseName")
        _save_path = os.getenv("database.savePath")
        _back_max = os.getenv("database.backMax")
        _reg_ex = os.getenv("database.regEx")
        _cron = os.getenv("database.cron")

        database_config.set_type(_type if _type != None else database_config.get_type())
        database_config.set_url(_url if _url != None else database_config.get_url())
        database_config.set_port(_port if _port != None else database_config.get_port())
        database_config.set_username(_username if _username != None else database_config.get_username())
        database_config.set_password(_password if _password != None else database_config.get_password())
        database_config.set_database_name(_database_name if _database_name != None else database_config.get_database_name())
        database_config.set_save_path(_save_path if _save_path != None else database_config.get_save_path())
        database_config.set_back_max(_back_max if _back_max != None else database_config.get_back_max())
        database_config.set_reg_ex(_reg_ex if _reg_ex != None else database_config.get_reg_ex())
        database_config.set_cron(_cron if _cron != None else database_config.get_cron())

        return database_config
