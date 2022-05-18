import logging
from rich.logging import RichHandler

import test_module

log_format = ''.join(['[%(asctime)s]', '|%(levelname)s|[%(module)s]::%(funcName)s()|%(message)s'])
# logging.basicConfig(level = logging.CRITICAL, format=log_format)

log = logging.getLogger()
# print(f'Handlers={logging.root.handlers}')
log.setLevel(logging.DEBUG)

hdlr = logging.StreamHandler()
# hdlr = RichHandler(rich_tracebacks=True)
hdlr.setFormatter(logging.Formatter(log_format))
hdlr.setLevel(logging.DEBUG)
log.addHandler(hdlr)

hdlr = logging.FileHandler('temp_log.txt', mode='w')
hdlr.setFormatter(logging.Formatter(log_format))
hdlr.setLevel(logging.WARNING)
log.addHandler(hdlr)

print(f'Logger={log.name}')
# print(f'Handlers={logging.root.handlers}')
# print(f'Handlers={log.handlers}')

log.debug("main debug msg")
log.info("main info msg")
log.warning("main warn msg")
log.error("main err msg")
log.critical("main crit msg")
print('---')

logging.getLogger('testmodule').setLevel(logging.ERROR)
test_module.stuff()
print('---')
try:
    print(2/0)
except ZeroDivisionError as e:
#     log.error(e, exc_info=True)
    log.exception(e)

