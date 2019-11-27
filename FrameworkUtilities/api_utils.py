"""
This module contains api utility functions.
"""

import logging
import requests
from traceback import print_stack
import FrameworkUtilities.logger_utility as log_utils


class APIUtilily:
    """
    This class includes basic reusable api utility helpers.
    """
    log = log_utils.custom_logger(logging.INFO)

    # def __init__(self):
    #     self.log = log_utils.custom_logger(logging.INFO)

    def get_api_response(self, endpoint):
        """
        This method is used to return the api response
        :return: This method return the api response
        """

        res = None
        try:
            # noinspection PyBroadException
            response = requests.get(endpoint)
            if response.status_code == 200:
                res = response
            else:
                res = None
        except Exception as ex:
            self.log.error("Failed to get the response.\n{}".format(ex))
            print_stack()

        return res
