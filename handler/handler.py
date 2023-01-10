from entity.config.database_config import DataBaseConfig
from handler.mysql_handler import MysqlHandler
from handler.oracle_handler import OracleHandler
class Handler():
    '''
    处理器
    '''
    def create_task(self, database_config:DataBaseConfig) :
        '''
        创建任务
        '''
        match database_config.get_type():
            case "MySQL": 
                self.create_task(MysqlHandler(), database_config)
            case "Oracle": 
                self.create_task(OracleHandler(), database_config)
            case "SQLServer":
                print("暂未开放")
            case "PostgreSQL":
                print("暂未开放")
            case "SQLite":
                print("暂未开放")
            case "Hive":
                print("暂未开放")

    
    def create_task(self, handler:MysqlHandler, database_config:DataBaseConfig):
        
        pass

    def create_task(self, handler:OracleHandler, database_config:DataBaseConfig):
        pass