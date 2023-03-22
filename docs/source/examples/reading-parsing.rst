Reading and Parsing
--------------------

Read Logs
~~~~~~~~~

..  code-block:: python

   from zapish_logger import read_log_file


   data = read_log_file('./logs.log')

   print(data)

Parse Logs
~~~~~~~~~~

..  code-block:: python

   import re
   from zapish_logger import read_log_file


   data = read_log_file('./logs.log')

   for log in data:
       if log.get('level') == 'DEBUG':
           print(log)

   regex = re.compile(r'.*L.*')

   for log in data:
       if re.match(regex, log.get('msg')):
           print(log)
