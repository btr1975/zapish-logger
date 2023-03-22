console_logger
--------------

New Console Logger
~~~~~~~~~~~~~~~~~~

..  code-block:: python

   from zapish_logger import console_logger


   logger = console_logger('great-logger')

   logger.info("HELLO")


Example Console Output
~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: bash

   {"level": "INFO", "ts": "2023-03-21 21:39:25,347", "caller": "great-logger", "msg": "HELLO"}
