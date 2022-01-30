import logging
from datetime import datetime
from pathlib import Path

from core.singleton import SingletonMeta


class LoggerCreator(metaclass=SingletonMeta):
    def __init__(self):
        self.file_name = Path.cwd() / f'log_{datetime.utcnow().strftime("%Y%m%d%H%M%S%f")}.log'
        self.logger = self.__get_logger()

    def __get_logger(self):
        logger = logging.getLogger('logger')
        file_handler = logging.FileHandler(self.file_name)
        file_handler.setFormatter(logging.Formatter(fmt='[%(asctime)s] [%(levelname)s] %(message)s'))
        logger.addHandler(file_handler)
        logger.setLevel(logging.ERROR)
        logger.setLevel(logging.INFO)
        return logger