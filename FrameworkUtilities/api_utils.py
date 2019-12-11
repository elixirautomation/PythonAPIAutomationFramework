"""
This module contains api utility functions.
"""

import logging
import requests
from traceback import print_stack
from requests.exceptions import HTTPError
import FrameworkUtilities.logger_utility as log_utils


class APIUtilily:
    """
    This class includes basic reusable api utility helpers.
    """
    log = log_utils.custom_logger(logging.INFO)

    def get_api_response(self, endpoint):
        """
        This method is used to return the api response
        :return: This method return the api response
        """

        res = None

        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            if response.status_code == 200:
                res = response
            else:
                res = None

        except HTTPError as http_err:
            self.log.error(f'HTTP Error occurred.\n{http_err}')
            print_stack()

        except Exception as ex:
            self.log.error(f'Failed to get the response, other error occurred.\n{ex}')
            print_stack()

        return res
