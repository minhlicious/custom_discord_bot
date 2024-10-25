from configparser import ConfigParser
from pathlib import Path


def GetConfig() -> ConfigParser:
    config = ConfigParser()
    config_path = Path("./config.ini")
    if not config_path.exists():
        raise Exception("config.ini does not exist")
    config.read(config_path)
    return config
