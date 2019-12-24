
import logging

from app.common.constants import SOME_VALUE

log = logging.getLogger("sample." + __name__)


def mod_func():
    return f"mod_func... some_value={SOME_VALUE}"


def get_value():
    return SOME_VALUE
