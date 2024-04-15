from selenium import webdriver
import pytest
from URLs import Urls

@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Urls.main_page)
    yield chrome_driver
    chrome_driver.quit()


