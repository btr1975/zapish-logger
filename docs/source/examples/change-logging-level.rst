Change Logging Level
--------------------

* Since this is just built on the built in logger it is simple.

..  code-block:: python

   import logging
   from json_logger import console_logger


   logger = console_logger('great-logger')

   logger.setLevel(logging.DEBUG)

   logger.debug("HELLO")
