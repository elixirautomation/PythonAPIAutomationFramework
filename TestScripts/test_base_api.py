""" This module contains all test cases."""

import sys
import logging
import unittest
import allure
import pytest
from BaseAPI.base_api import BaseAPI
from FrameworkUtilities.execution_status_utility import ExecutionStatus
import FrameworkUtilities.logger_utility as log_utils
from FrameworkUtilities.data_reader_utility import DataReader


@allure.story('Test Automation Demo for APIs')
@allure.feature('API Response Verification Using Requests')
@pytest.mark.usefixtures("rp_logger")
class BaseAPITests(unittest.TestCase):
    """
    This class contains the executable test cases.
    """

    data_reader = DataReader()

    def setUp(self):
        self.exe_status = ExecutionStatus()
        self.base_api = BaseAPI()
        self.log = log_utils.custom_logger(logging.INFO)

    def tearDown(self):
        # add db cleaning code here
        pass

    @pytest.fixture(autouse=True)
    def class_level_setup(self, request):
        """
        This method is used for one time setup of test execution process,
        which check for the test cases to run mentioned in the excel file.
        :return: it returns nothing
        """

        if self.data_reader.get_data(request.function.__name__, "Runmode") != "Y":
            pytest.skip("Excluded from current execution run.")

    @allure.testcase("Get All Users")
    @pytest.mark.smoke
    def test_verify_users(self, rp_logger):
        """
        This test is validating the users from api response. (positive scenario)
        :return: return test status
        """

        test_name = sys._getframe().f_code.co_name

        rp_logger.info("###### TEST EXECUTION STARTED :: " +
                       test_name + " ######")

        with allure.step("Get all users for this specific endpoint"):
            result = self.base_api.verify_users()
            self.exe_status.mark_final(test_step=test_name, result=result)

    @allure.testcase("Verify Valid User")
    @pytest.mark.regression
    def test_verify_valid_user(self, rp_logger):
        """
        This test is validating the users from api response. (positive scenario)
        :return: return test status
        """

        test_name = sys._getframe().f_code.co_name

        rp_logger.info("###### TEST EXECUTION STARTED :: " +
                       test_name + " ######")

        first_name = self.data_reader.get_data(test_name, 'FirstName')
        last_name = self.data_reader.get_data(test_name, 'LastName')
        email = self.data_reader.get_data(test_name, 'Email')

        with allure.step("Verify whether user exists"):
            result = self.base_api.verify_valid_user(
                email, first_name, last_name)
            self.exe_status.mark_final(test_step=test_name, result=result)

    @allure.testcase("Verify Invalid User")
    @pytest.mark.regression
    def test_verify_invalid_user(self, rp_logger):
        """
        This test is validating the users from api response. (negative scenario)
        :return: return test status
        """

        test_name = sys._getframe().f_code.co_name

        rp_logger.info("###### TEST EXECUTION STARTED :: " +
                       test_name + " ######")

        first_name = self.data_reader.get_data(test_name, 'FirstName')
        last_name = self.data_reader.get_data(test_name, 'LastName')
        email = self.data_reader.get_data(test_name, 'Email')

        with allure.step("Verify whether user exists"):
            result = self.base_api.verify_valid_user(
                email, first_name, last_name)
            self.exe_status.mark_final(test_step=test_name, result=result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
