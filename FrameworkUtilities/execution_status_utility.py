""" This module contains the methods to conclude the execution status. """

import pytest
import logging
from traceback import print_stack
import FrameworkUtilities.logger_utility as log_utils


class ExecutionStatus:

    """ This class contains the methods to conclude the execution status. """

    def __init__(self):
        self.result_list = []
        self.log = log_utils.custom_logger(logging.INFO)

    def set_result(self, result, test_name):
        """
        This method is used for setting the execution result.
        :param result: this parameter takes the execution status value pass/fail.
        :param test_name: this parameter takes the execution status description.
        :return: this method returns nothing.
        """

        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info(
                        "### STEP SUCCESSFUL :: " + test_name)
                else:
                    self.result_list.append("FAIL")
                    self.log.error("### STEP FAILED :: " + test_name)

            else:
                self.result_list.append("FAIL")
                self.log.error("### STEP FAILED :: " + test_name)
        except Exception as ex:
            self.result_list.append("FAIL")
            self.log.error("### EXCEPTION OCCURRED :: {}".format(ex))
            print_stack()

    def mark(self, test_step, result):
        """
        This method handles intermediate assertions and saves the result for final mark.
        :param result: this parameter takes the execution status value pass/fail.
        :param test_step: it takes the test case name value
        :return: this method returns nothing.
        """

        self.set_result(result=result, test_name=test_step)

    def mark_final(self, result, test_step):
        """
        This method handles final assertion and saves the result for final mark.
        :param test_step: it takes the test case name value
        :param result: this parameter takes the execution status value pass/fail.
        :return: this method returns nothing.
        """

        self.set_result(result, test_step)

        try:
            if "FAIL" in self.result_list:
                self.result_list.clear()
                assert True is False

            else:
                self.result_list.clear()
                assert True is True, "### TEST SUCCESSFUL :: " + test_step

        except Exception:
            pytest.fail("### TEST FAILED :: " + test_step, pytrace=False)

