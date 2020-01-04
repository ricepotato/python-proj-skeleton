import logging
import configparser

log = logging.getLogger("sample." + __name__)


class SomeClass(object):
    """ Test Some class """

    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read("conf/database.conf")

    def add(self, a, b):
        log.info(f"add ${a} + ${b} = ${a + b}")
        return a + b
