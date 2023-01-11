class DataBaseConfig() :

    _application_name = None
    _type = None
    _url = None
    _port = None
    _username = None
    _password = None
    _database_name = None
    _charset = None
    _save_path = None
    _back_max = 20
    _reg_ex = None
    _cron = None

    def __init__(self, application_name, type, url, port, username, password, database_name, charset, back_max, reg_ex, cron) -> None:
        ''' 初始化数据库配置类
        :param type:            数据库类型
        :param url:             数据库连接地址
        :param port:            数据库端口
        :param username:        数据库连接用户名
        :param password:        数据库连接密码
        :param database_name:   数据库名称
        :param database_name:   数据库名称
        :param charset:         数据库字符编码
        :param reg_ex:          数据库表过滤
        :param cron:            数据库备份时间表达式
        '''
        self._application_name = application_name
        self._type = type
        self._url = url
        self._port = port
        self._username = username
        self._password = password
        self._database_name = database_name
        self._charset = charset
        self._back_max = back_max
        self._reg_ex = reg_ex
        self._cron = cron

    def set_application_name(self, application_name:str) :
        self._application_name = application_name

    def get_application_name(self) :
        return self._application_name

    def set_type(self, type:str) :
        self._type = type

    def get_type(self) :
        return self._type

    def set_url(self, url:str) :
        self._url = url
        
    def get_url(self) :
        return self._url

    def set_port(self, port:str) :
        self._port = port
        
    def get_port(self) :
        return self._port

    def set_username(self, username:str) :
        self._username = username
        
    def get_username(self) :
        return self._username

    def set_password(self, password:str) :
        self._password = password
        
    def get_password(self) :
        return self._password

    def set_database_name(self, database_name:str) :
        self._database_name = database_name
        
    def get_database_name(self) :
        return self._database_name

    def set_charset(self, charset:str) :
        self._charset = charset
        
    def get_charset(self) :
        return self._charset

    def set_back_max(self, back_max:str) :
        self._back_max = back_max
        
    def get_back_max(self) :
        return self._back_max

    def set_reg_ex(self, reg_ex:str) :
        self._reg_ex = reg_ex
        
    def get_reg_ex(self) :
        return self._reg_ex

    def set_cron(self, cron:str) :
        self._cron = cron
        
    def get_cron(self) :
        return self._cron