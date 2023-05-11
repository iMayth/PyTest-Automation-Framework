from selenium.webdriver.common.by import By
from src.pom.pages.base_page import BasePageElement
from src.pom.pages.qlub_automation_task import QlubAutomationTask


class PageAsd(BasePageElement):
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


