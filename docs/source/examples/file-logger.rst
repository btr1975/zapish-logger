file_logger
------------

New File Logger
~~~~~~~~~~~~~~~

..  code-block:: python

   from json_logger import file_logger


   logger = file_logger('./logs.log', 'great-logger')

   logger.info("HELLO")


Add Console Output Also
~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: python

   from json_logger import file_logger, add_console_logger


   logger = file_logger('./logs.log', 'great-logger')

   add_console_logger(logger)

   logger.info("HELLO")

Example Log
~~~~~~~~~~~

..  code-block:: bash

   {"level": "INFO", "ts": "2023-03-21 21:34:27,676", "caller": "great-logger", "msg": "HELLO"}
   {"level": "INFO", "ts": "2023-03-21 21:34:44,444", "caller": "great-logger", "msg": "HELLO"}
   {"level": "INFO", "ts": "2023-03-21 21:34:45,714", "caller": "great-logger", "msg": "HELLO"}
   {"level": "INFO", "ts": "2023-03-21 21:37:51,135", "caller": "great-logger", "msg": "HELLO"}
