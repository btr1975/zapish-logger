"""
The JSON logger
"""
import logging
import sys


SCHEMA = '{"level": "%(levelname)s", "ts": "%(asctime)s", "caller": "%(name)s", "msg": "%(message)s"}'


def file_logger(path: str, name: str) -> logging.Logger:
    """Function to get a file logger

    :type path: String
    :param path: The full path to the log file Example: /tmp/some_log.log
    :type name: String
    :param name: The name of the logger

    :rtype: logging.Logger
    :returns: The logger
    """
    this_logger = logging.getLogger(name)
    logging.basicConfig(format=SCHEMA, filename=path)
    logging.getLogger().setLevel(logging.INFO)
    return this_logger


def console_logger(name: str) -> logging.Logger:
    """Function to get a console logger

    :type name: String
    :param name: The name of the logger

    :rtype: logging.Logger
    :returns: The logger
    """
    this_logger = logging.getLogger(name)
    logging.basicConfig(format=SCHEMA, stream=sys.stdout)
    logging.getLogger().setLevel(logging.INFO)
    return this_logger


def add_console_logger(root_logger: logging.Logger) -> None:
    """Function to add a console logger

    :type root_logger: logging.Logger
    :param root_logger: The logger to add console logger to

    :rtype: None
    :returns: Nothing it adds a console logger
    """
    if not isinstance(root_logger, logging.Logger):
        raise TypeError(f'root_logger must be of type logging.Logger but received a {type(root_logger)}')

    console_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(fmt=SCHEMA)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)
