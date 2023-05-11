import time

from selenium.webdriver.common.by import By
from src.pom.pages.base_page import BasePageElement
from src.pom.pages.qlub_automation_task import QlubAutomationTask


class CheckOutPage(BasePageElement):
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # pay_now = (By.XPATH, "//span[text()='Pay now ']")
    # split_bill = (By.XPATH, "//span[text()='Split bill']")
    # custom_amount = (By.ID, "select-custom")
    # set_amount = (By.CSS_SELECTOR, "input#fullWidth")
    # confirm_amount = (By.XPATH, "//span[text()='Confirm']")
    # select_tip = (By.XPATH, "//div[@class='MuiBox-root css-17oy29i']")
    # card_number = (By.ID, "checkout-frames-card-number")
    # expiry_date = (By.ID, "checkout-frames-expiry-date")
    # cvv = (By.ID, "checkout-frames-cvv")
    # pay = (By.XPATH, "//span[text()='Pay Now']")
    # success_message = (By.XPATH, "//p[text()='Payment was successful!']")
    #
    # def testing(self):
    #     self.click(self.pay_now)
    #     self.click(self.split_bill)
    #     self.click(self.custom_amount)
    #     self.send_keys(self.set_amount, "10")
    #     self.click(self.confirm_amount)
    #     time.sleep(3)
    #     self.click(self.select_tip)
    #     self.send_keys(self.card_number, "4242424242424242")
    #     self.send_keys(self.expiry_date, "0226")
    #     self.send_keys(self.cvv, "100")
    #     self.click(self.pay)
