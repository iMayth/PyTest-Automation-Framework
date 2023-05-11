import settings
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from src.pom.pages.page123 import PageAsd
from src.pom.pages.qlub_automation_task import QlubAutomationTask
from src.pom.pages.random_page import RandomPage

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=settings.browser)


@pytest.fixture
def get_browser(request):
    browser = request.config.getoption("--browser")
    return browser


@pytest.fixture
def get_driver(request, get_browser):
    global driver
    if get_browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    elif get_browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    elif get_browser == "headless":
        chrome_options = Options()
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--no-sandbox") # linux only
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    else:
        print("Driver not supported")
    driver.implicitly_wait(10)
    # Add in here each page from the POM in order to initialize the driver for each one.
    request.cls.qlub_automation_task = QlubAutomationTask(driver)
    driver.get(settings.url)
    yield driver
    driver.quit()
