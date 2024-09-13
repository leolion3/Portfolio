# Enhanced Logger Module

Provided here is a simple logger module that provides enhanced logging functionality.

## Requirements

The logger uses the `loguru` library as its backbone, which can be installed using

```bash
pip install loguru
```

and should be added to the project's requirements (or lock) file.

## Usage

The logger uses a singleton instance which can be referenced anywhere:

```python
import log_handler
from log_handler import Logger, Module


logger: Logger = log_handler.get_instance()
logger.info('Hello world!', module=Module.LOGGER)
```

Output:

```
2023-01-01 12:00:00.000 | INFO     | log_handler:__init__:155 - [LOGGER] Initialising logger...
2023-01-01 12:00:00.000 | INFO     | log_handler:info:122 - [LOGGER] Logger initialized.
2023-01-01 12:00:00.000 | INFO     | log_handler:info:122 - [LOGGER] Hello world!
```

## Adding modules

The logger prints log messages based on the provided module enum. If no module is specified, the log is printed without a `[Module]` prefix.

This prefix is meant to allow filtering logs easily based on module and functionality. To add modules, simply extend the `Module` class. For example:

```python
class Module(Enum):
    LOGGER = 'LOGGER'
    PPROC = 'Pre-Processor'
    MAIN = 'MAIN'
    API = 'REST'
    # ... More ...
```

Usage:

```python
logger.info('^ [::] 127.0.0.1 --> 127.0.0.1', module=Module.API)
```

Output:

```
2023-01-01 12:00:00.000 | INFO     | log_handler:info:122 - [REST] ^ [::] 127.0.0.1 --> 127.0.0.1
```

## Log file

The module automatically attempts to write the logs to a file called `application.log` within the directory it is placed (the path is dynamically altered). If undesired, the line

```python
self.__open_fp()
```

can be removed from the class' constructor.

## Setting and Changing Log Level

By default, the module runs in DEBUG mode, printing all logs. This can be changed through the environment variable `LOG_LEVEL`, which can be set to one of:

1. DEBUG: All logs are printed.
2. INFO: Info, warning and error logs are printed (debug logs are redacted).
3. WARNING: Warning and Error logs are printed.
4. SILENT: No logs are printed.

The log level can also be changed by calling the `change_log_level` method with the desired log level's name. Example, extending the previous demo:

```python
logger.change_log_level('INFO')
logger.debug('This message is redacted')
logger.info('Info works, debug does not')

logger.change_log_level('DEBUG')
logger.debug('Debug works again!')
```

Output:

```
2023-01-01 12:00:00.000 | INFO     | log_handler:info:143 - [LOGGER] Log level changed to INFO
2023-01-01 12:00:00.000 | INFO     | log_handler:info:143 - Info works, debug does not
2023-01-01 12:00:00.000 | INFO     | log_handler:info:143 - [LOGGER] Log level changed to DEBUG
2023-01-01 12:00:00.000 | DEBUG    | log_handler:debug:171 - Debug works again!
```
