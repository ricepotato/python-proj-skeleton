from app.common.mod import mod_func
from app.mod2 import mod_func as mod2_func
import logging

log = logging.getLogger("sample." + __name__)
log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)


def main():
    log.info("main...")
    res = mod_func()
    log.info(res)
    res = mod2_func()
    log.info(res)


if __name__ == "__main__":
    main()
