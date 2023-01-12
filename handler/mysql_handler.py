from entity.config.database_config import DataBaseConfig
import os, pymysql, re, time
from utils.logger_util import LoggerUtil

class MysqlHandler():
    '''
    mysql处理器
    '''
    _database_config = None

    def dump(self, database_config:DataBaseConfig):
        '''
        数据库备份
        '''
        logger = LoggerUtil().getLogger("database-backup")
        self._database_config = database_config
        backPath = os.path.join(os.path.dirname(os.path.realpath(__file__)).replace("handler", "dbback"), database_config.get_application_name())
        if not os.path.exists(backPath) :
            os.makedirs(backPath)
        regTables = self.filter_tables_by_regex(self.get_all_tables())
        if (regTables.isspace()) :
            logger.info("数据库名为：%s 过滤后需要备份的表为空！"%database_config.get_database_name())
            return
        backFileName = time.strftime("%Y-%m-%d-%H_%M_%S.sql", time.localtime())
        dump_sql = 'mysqldump --no-tablespaces -h%s -P%s -u%s -p%s %s %s > %s'%(
            self._database_config.get_host(),
            self._database_config.get_port(),
            self._database_config.get_username(),
            self._database_config.get_password(),
            self._database_config.get_database_name(),
            regTables,
            os.path.join(backPath, backFileName))

        if not os.system(dump_sql):
            logger.info("成功备份文件名为：%s \n备份表为： %s"%(backFileName, regTables))
        else:
            logger.error("备份表: %s 失败！"%(regTables))

    def filter_tables_by_regex(self, tables):
        '''
        根据RegEx匹配表名
        '''
        result = " "
        for table_name in tables:
            searchTable = re.match(self._database_config.get_table_regEx(), table_name.get("TABLE_NAME"), re.M|re.I).span()
            if searchTable and searchTable[1] == len(table_name.get("TABLE_NAME")):
                result = result + table_name.get("TABLE_NAME") + " "
        return result

    def get_all_tables(self):
        '''
        获取数据库的所有表名
        '''
        connect = pymysql.Connect(
            host=self._database_config.get_host(),
            port=self._database_config.get_port(),
            user=self._database_config.get_username(),
            password=self._database_config.get_password(),
            db=self._database_config.get_database_name()
        )
        cur = connect.cursor(cursor=pymysql.cursors.DictCursor)
        select_table_name_sql = 'SELECT table_name FROM information_schema.tables where table_schema="%s";'%(self._database_config.get_database_name())
        cur.execute(select_table_name_sql)
        tables = cur.fetchall()
        connect.close()
        return tables