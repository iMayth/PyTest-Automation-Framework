from selenium.webdriver.common.by import By

from src.pom.pages.base_page import BasePageElement


class RandomPage(BasePageElement):

    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver

