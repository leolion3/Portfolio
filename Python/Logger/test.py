#!/usr/bin/env python3
import log_handler
from log_handler import Logger, Module


logger: Logger = log_handler.get_instance()
logger.info('Hello world!', module=Module.LOGGER)

logger.change_log_level('INFO')
logger.debug('This message is redacted')
logger.info('Info works, debug does not')

logger.change_log_level('DEBUG')
logger.debug('Debug works again!')