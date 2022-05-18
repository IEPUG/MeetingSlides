import logging
from rich.logging import RichHandler


log_format = ''.join(['[%(asctime)s]', '|%(levelname)s|[%(module)s]::%(funcName)s()|%(message)s'])
logging.basicConfig(level = logging.INFO, format=log_format, handlers=[RichHandler()])

log = logging.getLogger()
log.setLevel(logging.DEBUG)

print(f'Logger={log.name}')

log.debug("main debug msg")
log.info("main info msg")
log.warning("main warn msg")
log.error("main err msg")
log.critical("main crit msg")

print('---')
try:
    print(2/0)
except ZeroDivisionError as e:
#     log.error(e, exc_info=True)
    log.exception(e)

