import os
from .logger import init_logger
import logging
from .config import read_yaml

env = os.environ["ENV"]
settings = read_yaml(f"{os.getcwd()}/src/common/yaml_configs/{env}.yaml")

# loggerの初期化
init_logger(settings.LOGGER_CONFIG_PATH)
logger = logging.getLogger(__name__)