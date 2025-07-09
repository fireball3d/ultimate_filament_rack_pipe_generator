import logging
import os

logger = logging.getLogger(__name__)


def is_runner():
    """
    Determine if CICD Runner or not

    :return Boolean
    """

    logger.debug(f"Current Working Directory {os.getcwd()}")

    results = "CI" in os.environ
    logger.info(f"is_runner {results}")

    return results


# def is_github():
#     """
#     Determine if on Github Runner

#     :return Boolean
#     """

#     results = "GITHUB_ACTIONS" in os.environ
#     logger.info(f"is_github {results}")

#     return results
