from loader.environment_loader import EnvironmentLoader
from loader.config_loader import ConfigLoader
import os

configName = "application.yml"
currentPath = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(currentPath, configName)

database_config = ConfigLoader().load_config(configPath)
database_config = EnvironmentLoader().load_config(database_config)
