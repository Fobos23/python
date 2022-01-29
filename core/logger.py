import logging
from datetime import datetime
from pathlib import Path

from core.singleton import SingletonMeta


class LoggerCreator(metaclass=SingletonMeta):
    def __init__(self):
        self.__file_name = f'log_{datetime.utcnow().strftime("%Y%m%d%H%M%S%f")}.log'
        self.logger = self.__get_logger()

    def __get_logger(self):
        logger = logging.getLogger('logger')
        file_handler = logging.FileHandler(self.__file_name)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger