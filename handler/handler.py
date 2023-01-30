from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from entity.config.database_config import DataBaseConfig
from entity.config.application_config import ApplicationConfig
from handler.mysql_handler import MysqlHandler
from handler.oracle_handler import OracleHandler
from utils.logger_util import LoggerUtil
import os

class Handler():
    '''
    处理器
    '''
    _sched = BlockingScheduler()
    _database_config = None
    _application_config = None
    _logger = LoggerUtil().getLogger("database-backup")
    _create_dump_flag = False

    def create_task(self, database_config:DataBaseConfig, application_config:ApplicationConfig) :
        '''
        创建任务
        '''
        
        self._database_config = database_config
        self._application_config = application_config

        dbType = self._database_config.get_type()
        self._logger.info("开始创建定时备份数据库为 %s 类型任务"%dbType)
        if "MySQL" == dbType:
            self._create_dump_flag = self.create_mysql_task(MysqlHandler())
        elif "Oracle" == dbType:
            self._create_dump_flag = self.create_oracle_task(OracleHandler())
        else:
            self._logger.info("%s 类型数据库备份暂未开放！"%dbType)

        if self._create_dump_flag:
            self.create_clear_back_task()

        self._logger.info("创建定时备份数据库为 %s 类型任务成功"%dbType)
        self._logger.info("开始执行定时任务……，定时配置为 %s"%self._database_config.get_cron())
        self._sched.start()
        
    def create_mysql_task(self, handler:MysqlHandler):
        '''
        创建mysql定时备份任务
        '''
        if not self.check_database_connect(handler): return False
        try:
            self._sched.add_job(func=handler.dump, trigger=CronTrigger.from_crontab(self._database_config.get_cron()) ,args=(self._database_config,self._application_config,))
            return True
        except Exception:
            self._logger.error("创建定时备份Mysql任务失败！")
            return False
    
    def create_oracle_task(self, handler:OracleHandler):
        '''
        创建Oracle定时任务
        '''
        pass

    def check_database_connect(self, handler):
        '''
        测试数据库的连通性
        '''
        connect = handler.get_connection()
        if connect == None:
            self._logger.error("测试数据库连接失败，连接信息：%s"%self._database_config.__dict__)
            return False
        else:
            self._logger.info("测试数据库连接成功，连接信息：%s"%self._database_config.__dict__)
            handler.close_conection(connect)
            return True

    def create_clear_back_task(self):
        '''
        创建定时清除备份文件任务
        '''
        self._logger.info("开始创建定期清理备份文件任务，最大保留备份文件数为 %s"%self._database_config.get_back_max())
        self._sched.add_job(func=self.clear_back, trigger=CronTrigger.from_crontab(self._database_config.get_cron()))
        self._logger.info("创建定期清理备份文件任务成功，最大保留备份文件数为 %s"%self._database_config.get_back_max())

    def clear_back(self):
        '''
        根据配置保留备份最大数，清除多余备份文件
        '''
        currentPath = os.path.dirname(os.path.realpath(__file__))
        dbbackPath = os.path.join(currentPath.replace("handler","dbback"), self._application_config.get_name())
        backFiles = os.listdir(dbbackPath)
        count = len(backFiles) - int(self._database_config.get_back_max())
        clearFiles = []
        if count > 0:
            for i in range(count):
                os.remove(os.path.join(dbbackPath, backFiles[i]))
                clearFiles.append(backFiles[i])
        self._logger.info("成功清理 %s 个文件，清理的备份文件有%s。"%(len(clearFiles), clearFiles))
        self._logger.info("系统目前保留备份文件有 %s 个，保留文件有 %s。"%(len(os.listdir(dbbackPath)), os.listdir(dbbackPath)))
            
