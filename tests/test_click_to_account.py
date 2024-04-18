from locators import Locators
from settings import Urls
from data import User
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import pytest

class TestClickToAccont:
    @pytest.mark.usefixtures('driver')
    def test_click_button_personal(self, driver):
        driver.get(Urls.main_page)
        driver.find_element(*Locators.LOGIN_MAINPAGE_BUTTON).click()
        WebDriverWait(driver, 5).until(ec.url_matches(Urls.login_page))

        email = driver.find_element(*Locators.EMAIL_LOGINPAGE_INPUT)
        email.send_keys(User.test_email)

        password = driver.find_element(*Locators.PASSWORD_LOGINPAGE_INPUT)
        password.send_keys(User.test_password)

        driver.find_element(*Locators.GO_BUTTON).click()

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        assert WebDriverWait(driver, 5).until(ec.url_matches(Urls.profile_page))
