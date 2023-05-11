import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import actions, keys
from selenium.webdriver.common.by import *
from src.pom.pages.base_page import BasePageElement


class QlubAutomationTask(BasePageElement):
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    pay_now = (By.XPATH, "//span[text()='Pay now ']")
    split_bill = (By.XPATH, "//span[text()='Split bill']")
    custom_amount = (By.ID, "select-custom")
    set_amount = (By.CSS_SELECTOR, "input#fullWidth")
    confirm_amount = (By.XPATH, "//span[text()='Confirm']")
    select_tip = (By.XPATH, "//div[@class='MuiBox-root css-17oy29i']")
    card_number = (By.ID, "checkout-frames-card-number")
    expiry_date = (By.ID, "checkout-frames-expiry-date")
    cvv = (By.ID, "checkout-frames-cvv")
    pay = (By.XPATH, "//span[text()='Pay Now']")
    success_message = (By.XPATH, "//p[text()='Payment was successful!']")

    def split_the_bill(self):
        self.click(self.pay_now)
        self.click(self.split_bill)
        self.click(self.custom_amount)
        self.send_keys(self.set_amount, "10")
        self.click(self.confirm_amount)
        time.sleep(2)

    def include_a_tip(self):
        self.click(self.select_tip)
        time.sleep(2)

    def pay_with_card_information(self):
        iframe_cn = self.driver.find_element_by_xpath("/html//iframe[@id='cardNumber']")
        self.driver.switch_to.frame(iframe_cn)
        self.send_keys(self.card_number, "4242424242424242")
        self.driver.switch_to.default_content()
        iframe_ed = self.driver.find_element_by_xpath("/html//iframe[@id='expiryDate']")
        self.driver.switch_to.frame(iframe_ed)
        self.send_keys(self.expiry_date, "0226")
        self.driver.switch_to.default_content()
        iframe_cvv = self.driver.find_element_by_xpath("/html//iframe[@id='cvv']")
        self.driver.switch_to.frame(iframe_cvv)
        self.send_keys(self.cvv, "100")
        self.driver.switch_to.default_content()
        self.click(self.pay)

    def message_is_displayed(self):
        self.wait_element_visible(self.success_message)
        return self.is_displayed(self.success_message)










