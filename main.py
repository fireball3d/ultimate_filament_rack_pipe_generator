#! /usr/bin/env python3
import logging

import src.common.logs

# Setup Logger
src.common.logs.set_log_format()
logger = logging.getLogger(__name__)


def main():
    logger.info("Hello from ultimate-filament-rack-pipe-generator!")


if __name__ == "__main__":
    main()
