import os
import time

from enum import Enum


class LogLevel(Enum):
    DEBUG = 0
    DETAIL = 1
    INFO = 2
    WARNING = 3
    ERROR = 4


class Logger:
    # 支持文件路径或者直接给定文件对象
    def __init__(self, level: LogLevel, file):
        self.level = level
        self.file = file
        if isinstance(self.file, str):
            os.makedirs(os.path.split(self.file)[0], exist_ok=True)

    def log(self, level: LogLevel, msg):
        if level.value < self.level.value:
            return
        if isinstance(self.file, str):
            with open(self.file, 'a') as f:
                self.__real_do_log(level, msg, f)
        else:
            self.__real_do_log(level, msg, self.file)
            self.file.flush()

    @staticmethod
    def __real_do_log(level, msg, file):
        from threading import current_thread
        print(f'[{current_thread().name}][{time.strftime("%Y-%m-%d %H:%M:%S")}][{level.name}] {msg}', file=file)


logger_singleton = None


def get_logger():
    global logger_singleton
    from app.config.config import log_file, log_level

    if logger_singleton is None:
        logger_singleton = Logger(log_level, log_file)
    return logger_singleton
