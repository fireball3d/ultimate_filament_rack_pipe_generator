import logging

from . import cicd


def set_log_format():
    if cicd.is_runner():
        log_format = "%(levelname)s: [%(name)s.%(funcName)s] %(message)s"
    else:
        log_format = "%(levelname)s: %(message)s"

    logging.basicConfig(format=log_format, level=logging.INFO)
