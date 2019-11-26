"""
This module contains config utility functions.
"""

import os
import json
import time
import logging
from traceback import print_stack
from configparser import ConfigParser
import FrameworkUtilities.logger_utility as log_utils


class ConfigUtility:
    """
    This class includes basic reusable config_helpers.
    """

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self):
        # self.log = log_utils.custom_logger(logging.INFO)
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.config_path = os.path.join(self.cur_path, r"../ConfigFiles/config.ini")

    def load_properties_file(self):
        """
        This method loads the properties/ini file
        :return: this method returns config reader instance.
        """

        config = None
        try:
            # noinspection PyBroadException
            config = ConfigParser()
            config.read(self.config_path)

        except Exception as ex:
            self.log.error("Failed to load ini/properties file.", ex)
            print_stack()

        return config

    def change_properties_file(self, section, property_name, property_value):
        """
        This method is used to change the property value
        :param section: property section in ini file
        :param property_name: property name to change
        :param property_value: property value to set
        :return: it returns boolean value for successful change property operation
        """
        try:
            config = self.load_properties_file()
            config[section][property_name] = property_value

            with open(self.config_path, 'w') as configfile:
                config.write(configfile)

            time.sleep(1)

            return True

        except Exception as ex:
            self.log.error("Failed to change ini/properties file.", ex)
            print_stack()
            return False

    def load_json_file(self, file_path):
        """
        This method is used to load the json file
        :param file_path: path for the json file
        :return: data from the json file
        """
        try:
            with open(file_path, "r") as jsonFile:
                data = json.load(jsonFile)

            return data
        except Exception as Ex:
            self.log.error("Failed to load json file.", Ex)
            print_stack()
            return None