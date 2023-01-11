from entity.config.database_config import DataBaseConfig
import os, pymysql, re, time

class MysqlHandler():
    '''
    mysql处理器
    '''
    _database_config = None

    def dump(self, database_config:DataBaseConfig):
        '''
        数据库备份
        '''
        self._database_config = database_config
        backPath = os.path.join(os.path.dirname(os.path.realpath(__file__)).replace("handler", "dbback"), database_config.get_application_name())
        if not os.path.exists(backPath) :
            os.makedirs(backPath)
        backFileName = time.strftime("%Y-%m-%d-%H_%M_%S.sql", time.localtime())
        dump_sql = 'mysqldump -h %s -p %s -u %s -p %s %s %s > %s'%(
            self._database_config.get_url(),
            self._database_config.get_port(),
            self._database_config.get_username(),
            self._database_config.get_password(),
            self._database_config.get_database_name(),
            self.filter_tables_by_regex(self.get_all_tables()),
            os.path.join(backPath, backFileName))

        if os.system(dump_sql):
            print("成功备份")
        else:
            print("备份失败")

    def filter_tables_by_regex(self, tables):
        '''
        根据RegEx匹配表名
        '''
        result = " "
        for table_name in tables:
            if re.search(self._database_config.get_reg_ex(), table_name.get("TABLE_NAME")) == table_name:
                result = result + table_name + " "
        return result

    def get_all_tables(self):
        '''
        获取数据库的所有表名
        '''
        connect = pymysql.Connect(
            host=self._database_config.get_url(),
            port=self._database_config.get_port(),
            user=self._database_config.get_username(),
            password=self._database_config.get_password(),
            db=self._database_config.get_database_name()
        )
        cur = connect.cursor(cursor=pymysql.cursors.DictCursor)
        select_table_name_sql = 'SELECT table_name FROM information_schema.tables where table_schema="%s";'%(self._database_config.get_database_name())
        cur.execute(select_table_name_sql)
        talbes = cur.fetchall()
        connect.close()
        return talbes