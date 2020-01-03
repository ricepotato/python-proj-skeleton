import logging

log = logging.getLogger("sample." + __name__)


class SomeClass(object):
    """ Test Some class """

    def add(self, a, b):
        log.info(f"add ${a} + ${b} = ${a + b}")
        return a + b
