from app.common.mod import mod_func
from app.mod2 import mod_func as mod2_func
import logging

log = logging.getLogger("sample." + __name__)
stream_handler = logging.StreamHandler()
format_str = "[%(levelname)s]|%(filename)s:%(lineno)s] %(asctime)s : %(message)s"
formatter = logging.Formatter(format_str)
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)
log.setLevel(logging.INFO)


def main():
    log.info("main...")
    res = mod_func()
    log.info(res)
    res = mod2_func()
    log.info(res)


if __name__ == "__main__":
    main()
