file_and_console_logger
-------------------------

New File and Console Logger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: python

   from zapish_logger import file_and_console_logger


   logger = file_and_console_logger('./logs.log', 'great-logger')

   logger.info("HELLO")


Example File and Console Output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: bash

   {"level": "INFO", "ts": "2023-03-21 21:39:25,347", "caller": "great-logger", "msg": "HELLO"}
