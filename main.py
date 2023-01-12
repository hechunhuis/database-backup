from entity.config.database_config import DataBaseConfig
from utils.logger_util import LoggerUtil
from handler.handler import Handler
import os

logger = LoggerUtil().getLogger("database-backup")
logger.info('''\n                 %@@@@@@@@@@@@@@%
             @@@@@@@          @@@@@@@
          @@@@*                    *@@@@
       @@@@                            @@@@
     @@@@                                @@@@
    @@@            @@@@@@@@@@@@            @@@
  ;@@@         @@@@@@@@@@@@@@@@@@@          @@@;
 ;@@*        @@@@@@@          @@@@@@@        *@@;
 @@@        @@@@@                @@@@@ @@@*   @@@
@@@        @@@@                 @@@@@@@@@@     @@@
@@        @@@@                 @@*@@@@@@@       @@
@@        @@@@                    @@@@*@@       @@
@@        @@@                                   @@
@@        @@@*                      %@*@        @@
@@       @@@@@@@@@                  @@@@        @@
@@@     @@@@@@@@@@*                @@@@@       @@@
@@@    @@@@@@@@@                  @@@@@        @@@
 @@@    @@% %@@@@@              @@@@@@        @@@
  @@@         @@@@@@@@@    @@@@@@@@@         @@@
   @@@           @@@@@@@@@@@@@@@@           @@@
     @@@              @@@@@@              @@@
      @@@@                              @@@@
        @@@@@                        @@@@@
           @@@@@@                @@@@@@
               @@@@@@@@@@@@@@@@@@@@''')
logger.info("application start……")
configPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "application.yml")
Handler().create_task(DataBaseConfig(configPath))
logger.info("application success")