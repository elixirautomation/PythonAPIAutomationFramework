"""This module is used for main page objects."""

import logging
from FrameworkUtilities.config_utility import ConfigUtility
from FrameworkUtilities.api_utils import APIUtilily
import FrameworkUtilities.logger_utility as log_utils


class BaseAPI:
    """This class defines the method and element identifications for main page."""

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self):
        self.config = ConfigUtility()
        self.api = APIUtilily()
        self.prop = self.config.load_properties_file()
        # self.log = log_utils.custom_logger(logging.INFO)

    def verify_users(self):
        """
        This function is used to verify users
        :return: this function returns boolean status of element located
        """
        result = False
        res = self.api.get_api_response(
            endpoint=self.prop.get('RAFT', 'base_api'))
        if res is not None:
            res = res.json()
            self.log.info(res)
            result = True

        return result

    def verify_valid_user(self, email, first_name, last_name):
        """
        This function is used to verify email and username of a particular user
        :param last_name: user first name
        :param first_name: user last name
        :param email: user email address
        :return: status of the valid user
        """
        result = False
        res = self.api.get_api_response(
            endpoint=self.prop.get('RAFT', 'base_api'))
        if res is not None:
            res = res.json()
            self.log.info(res)

            if email == res['data'][0]['email'] and \
                    first_name == res['data'][0]['first_name'] and \
                    last_name == res['data'][0]['last_name']:
                result = True

        return result
