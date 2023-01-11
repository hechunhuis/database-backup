from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from entity.config.database_config import DataBaseConfig
from handler.mysql_handler import MysqlHandler
from handler.oracle_handler import OracleHandler
from utils.logger_util import LoggerUtil

class Handler():
    '''
    处理器
    '''
    _sched = BlockingScheduler()
    _database_config = None
    _logger = LoggerUtil().getLogger("database-backup")

    def create_task(self, database_config:DataBaseConfig) :
        '''
        创建任务
        '''
        self._database_config = database_config
        match self._database_config.get_type():
            case "MySQL": 
                self.create_mysql_task(MysqlHandler())
            case "Oracle": 
                self.create_oracle_task(OracleHandler())
            case "SQLServer":
                print("暂未开放")
            case "PostgreSQL":
                print("暂未开放")
            case "SQLite":
                print("暂未开放")
            case "Hive":
                print("暂未开放")

    def create_mysql_task(self, handler:MysqlHandler):
        self._logger.info("create schedule task ……")
        self._sched.add_job(handler.dump(self._database_config), CronTrigger.from_crontab(self._database_config.get_reg_ex()))
        self._logger.info("create schedule success")

    def create_oracle_task(self, handler:OracleHandler):
        pass
