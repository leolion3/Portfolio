#!/usr/bin/env python3
"""
Open-Source log handler module by Leonard Haddad, 2023.
Provided in accords with the MIT License.
More on GitHub at https://leolion.tk/
"""
import os
from enum import Enum
from typing import TextIO, Optional
from loguru import logger

LOGFILE: str = os.getenv('LOGFILE') or os.path.join(os.path.dirname(os.path.abspath(__file__)), 'application.log')
LOG_LEVEL: str = os.getenv('LOG_LEVEL') or 'DEBUG'


class Module(Enum):
    LOGGER = 'LOGGER'
    # Add your modules here in the format module_enum: 'module_description'


class LogType(Enum):
    ERROR = '[ERROR]'
    INFO = '[INFO]'
    DEBUG = '[DEBUG]'
    WARN = '[WARNING]'


class Logger:

    @staticmethod
    def __get_log_level() -> int:
        """
        Get the current log level.
        Possible values:
        - INFO (or empty) - info + err
        - Warning - warning + info + err
        - Silent - err only
        - Debug - everything
        """
        global LOG_LEVEL
        # Info
        if not len(LOG_LEVEL) or 'info' == LOG_LEVEL.lower():
            return 0
        # Silent
        if 'silent' == LOG_LEVEL.lower():
            return -1
        # Warning
        if 'warning' == LOG_LEVEL.lower():
            return 1
        # Debug
        return 2

    def change_log_level(self, log_level: str) -> None:
        """
        Update the log level.
        :param log_level: the new log level (info/silent/warn/debug).
        :return:
        """
        # Info
        if not len(log_level) or 'info' == log_level.lower():
            self.__log_level = 0
        # Silent
        elif 'silent' == log_level.lower():
            self.__log_level = -1
        # Warning
        elif 'warning' == log_level.lower():
            self.__log_level = 1
        # Debug
        else:
            self.__log_level = 2
        self.info('Log level changed to',
                  log_level, module=Module.LOGGER)

    @staticmethod
    def __handle_args(*args) -> str:
        return ' '.join([str(val) for val in args])

    def __open_fp(self) -> None:
        """
        Opens the file pointer to the specified log file.
        """
        if not LOGFILE:
            raise Exception('Logfile not specified! Running in console-mode only.')
        self.__fp: TextIO = open(LOGFILE, 'a+')

    def __write_log(self, message: str, mtype: LogType) -> None:
        """
        Write logging message to logfile.
        :param message: Message to write.
        :param mtype: The log message type.
        """
        if self.__fp is None:
            return
        message = ' '.join([mtype.value, message])
        self.__fp.write(f'{message}\n')
        self.__fp.flush()

    @staticmethod
    def __build_message(message: str, module: Module) -> str:
        """
        Build the text log message.
        :param message: The message to log.
        :param module: The module that logged the message.
        :return the message to log.
        """
        if not module:
            return message
        return ' '.join([f'[{module.value}]', message])

    def error(self, message: str, *args, module: Module = None) -> None:
        """
        Log an error message.
        :param message: The message to log.
        :param module: The module that logged the error.
        :return:
        """
        try:
            message = str(message) + ' ' + self.__handle_args(*args)
            msg = self.__build_message(message=message, module=module)
            logger.error(msg)
            self.__write_log(message=msg, mtype=LogType.ERROR)
        except Exception as e:
            logger.error('Error writing log. Trace: {}'.format(e))

    def info(self, message: str, *args, module: Module = None) -> None:
        """
        Log an info message.
        :param message: The message to log.
        :param module: The module that logged the info message.
        :return:
        """
        try:
            if self.__log_level < 0:
                return
            message = str(message) + ' ' + self.__handle_args(*args)
            msg = self.__build_message(message=message, module=module)
            logger.info(msg)
            self.__write_log(message=msg, mtype=LogType.INFO)
        except Exception as e:
            self.error('Error writing info log. Trace:', e, module=Module.LOGGER)

    def warning(self, message: str, *args, module: Module = None) -> None:
        """
        Log a warning message.
        :param message: The message to log.
        :param module: The module that logged the message.
        :return:
        """
        try:
            if self.__log_level < 1:
                return
            message = str(message) + ' ' + self.__handle_args(*args)
            msg = self.__build_message(message=message, module=module)
            logger.warning(msg)
            self.__write_log(message=msg, mtype=LogType.WARN)
        except Exception as e:
            self.error('Error writing warning log. Trace:', e, module=Module.LOGGER)

    def debug(self, message: str, *args, module: Module = None) -> None:
        """
        Log a debug message.
        :param message: The message to log.
        :param module: The module that logged the message.
        :return:
        """
        try:
            if self.__log_level < 2:
                return
            message = str(message) + ' ' + self.__handle_args(*args)
            msg = self.__build_message(message=message, module=module)
            logger.debug(msg)
            self.__write_log(message=msg, mtype=LogType.DEBUG)
        except Exception as e:
            self.error('Error writing debug log. Trace:', e, module=Module.LOGGER)

    def __init__(self):
        self.__fp: Optional[TextIO] = None
        logger.info(self.__build_message(message='Initialising logger...', module=Module.LOGGER))
        self.__log_level = self.__get_log_level()
        try:
            self.__open_fp()
            self.info(message='Logger initialized.', module=Module.LOGGER)
        except Exception as e:
            self.error(message=f'Error occurred! Logger running without caching. Trace: {e}', module=Module.LOGGER)


log: Logger = Logger()
