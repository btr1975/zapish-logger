custom_logger
-------------------------

New Custom Logger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: python

   from zapish_logger import custom_logger, LoggingConfig


    more_formats = {
        'moo': 'MOO: %(name)s %(asctime)s - %(levelname)s - %(message)s',
    }

    logging_config = LoggingConfig(custom_logging_formatters=more_formats)

    logging_config.add_console_handler(log_format='moo')

    logging_config.add_file_handler(path=path, log_format='clean')

    logger = custom_logger(logging_config=logging_config, name='great-logger')

    logger.info("HELLO")


Example Console Output
~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: bash

   MOO: great-logger 2024-03-16 21:47:32,720 - INFO - HELLO

Example File Output
~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: bash

   [2024-03-16 21:50:42,211] INFO:great-logger - HELLO
