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
        dbType = self._database_config.get_type()
        if "MySQL" == dbType:
            self.create_mysql_task(MysqlHandler())
        elif "Oracle" == dbType:
            self.create_oracle_task(OracleHandler())
        else:
            self._logger.info("%s 类型数据库备份暂未开放！"%dbType)

    def create_mysql_task(self, handler:MysqlHandler):
        self._logger.info("create schedule task ……")
        self._sched.add_job(func=handler.dump, trigger=CronTrigger.from_crontab(self._database_config.get_cron()) ,args=(self._database_config,))
        self._sched.start()
        self._logger.info("create schedule success")

    def create_oracle_task(self, handler:OracleHandler):
        pass
