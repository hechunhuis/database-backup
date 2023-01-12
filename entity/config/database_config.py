from utils.logger_util import LoggerUtil
import yaml, os

class DataBaseConfig() :

    _application_name = None
    _type = None
    _host = None
    _port = None
    _username = None
    _password = None
    _database_name = None
    _charset = None
    _save_path = None
    _back_max = 20
    _table_regEx = None
    _cron = None

    def __init__(self, configPath) -> None:
        '''
        初始化信息
        '''
        self.load_config(configPath=configPath)
        self.load_env()

    def load_config(self, configPath) :
        configInfo = open(configPath, 'r', encoding='utf-8').read()
        configInfoDict = yaml.load(configInfo, Loader=yaml.FullLoader)
        logger = LoggerUtil().getLogger("database-backup")
        logger.info("load application file success!")
        logger.info(configInfoDict)
        self._application_name = configInfoDict.get("database").get("application").get("name")
        self._type = configInfoDict.get("database").get("type")
        self._host = configInfoDict.get("database").get("host")
        self._port = configInfoDict.get("database").get("port")
        self._username = configInfoDict.get("database").get("username")
        self._password = configInfoDict.get("database").get("password")
        self._database_name = configInfoDict.get("database").get("databaseName")
        self._charset = configInfoDict.get("database").get("charset")
        self._back_max = configInfoDict.get("database").get("backMax")
        self._table_regEx = configInfoDict.get("database").get("table").get("regEx")
        self._cron = configInfoDict.get("database").get("cron")

    def load_env(self) :
        logger = LoggerUtil().getLogger("database-backup")
        logger.info("load environment ……")
        _application_name = os.getenv("database.application.name")
        _type = os.getenv("database.type")
        _host = os.getenv("database.host")
        _port = os.getenv("database.port")
        _username = os.getenv("database.username")
        _password = os.getenv("database.password")
        _database_name = os.getenv("database.databaseName")
        _charset = os.getenv("database.charset")
        _back_max = os.getenv("database.backMax")
        _table_regEx = os.getenv("database.table.regEx")
        _cron = os.getenv("database.cron")

        self._application_name = _application_name if _application_name != None else self._application_name
        self._type = _type if _type != None else self._type
        self._host = _host if _host != None else self._host
        self._port = _port if _port != None else self._port
        self._username = _username if _username != None else self._username
        self._password = _password if _password != None else self._password
        self._database_name = _database_name if _database_name != None else self._database_name
        self._charset = _charset if _charset != None else self._charset
        self._back_max = _back_max if _back_max != None else self._back_max
        self._table_regEx = _table_regEx if _table_regEx != None else self._table_regEx
        self._cron = _cron if _cron != None else self._cron

        logger.info(self.__dict__)
        logger.info("load environment success!")

    def set_application_name(self, application_name:str) :
        self._application_name = application_name

    def get_application_name(self) :
        return self._application_name

    def set_type(self, type:str) :
        self._type = type

    def get_type(self) :
        return self._type

    def set_host(self, host:str) :
        self._host = host
        
    def get_host(self) :
        return self._host

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

    def set_table_regEx(self, table_regEx:str) :
        self._table_regEx = table_regEx
        
    def get_table_regEx(self) :
        return self._table_regEx

    def set_cron(self, cron:str) :
        self._cron = cron
        
    def get_cron(self) :
        return self._cron
