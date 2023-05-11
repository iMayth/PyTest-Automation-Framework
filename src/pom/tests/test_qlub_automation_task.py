import pytest

from src.pom.tests.Testbase import BaseTest


class TestQlubAutomationTask(BaseTest):

    def test_pay_the_bill_and_verify(self):
        """
        Given User is on the checkout page
        When User splits and pays a custom amount
        Then User includes a tip
        And User enters card information and clicks pay
        And User is able to see success message on the successfull payment page
        """

        self.qlub_automation_task.split_the_bill()
        self.qlub_automation_task.include_a_tip()
        self.qlub_automation_task.pay_with_card_information()
        assert self.qlub_automation_task.message_is_displayed() == True
