""" This module contains all test cases."""

import sys
import allure
import pytest
from APIObjects.base_api import BaseAPI
from FrameworkUtilities.execution_status_utility import ExecutionStatus
from FrameworkUtilities.data_reader_utility import DataReader

exe_status = ExecutionStatus()
base_api = BaseAPI()
data_reader = DataReader()


@pytest.mark.usefixtures('initialize')
class TestAPI:

    @pytest.fixture(scope='function')
    def initialize(self, rp_logger):
        exe_status.__init__()

        def cleanup():
            # data cleaning steps to be written here
            rp_logger.info('Cleaning Test Data.')
        yield
        cleanup()

    @pytest.fixture(autouse=True)
    def class_level_setup(self, request):
        """
        This method is used for one time setup of test execution process,
        which check for the test cases to run mentioned in the excel file.
        :return: it returns nothing
        """

        if data_reader.get_data(request.function.__name__, "Runmode") != "Y":
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
            result = base_api.verify_users()
            exe_status.mark_final(test_step=test_name, result=result)

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

        first_name = data_reader.get_data(test_name, 'FirstName')
        last_name = data_reader.get_data(test_name, 'LastName')
        email = data_reader.get_data(test_name, 'Email')

        with allure.step("Verify whether user exists"):
            result = base_api.verify_valid_user(
                email, first_name, last_name)
            exe_status.mark_final(test_step=test_name, result=result)

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

        first_name = data_reader.get_data(test_name, 'FirstName')
        last_name = data_reader.get_data(test_name, 'LastName')
        email = data_reader.get_data(test_name, 'Email')

        with allure.step("Verify whether user exists"):
            result = base_api.verify_valid_user(
                email, first_name, last_name)
            exe_status.mark_final(test_step=test_name, result=result)
