from locators import Locators
from URLs import Urls
from data import User
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import pytest

class TestLogIn:
    @pytest.mark.usefixtures('driver')
    def test_login_button_mainpage(self, driver):
        driver.get(Urls.main_page)
        driver.find_element(*Locators.LOGIN_MAINPAGE_BUTTON).click()
        WebDriverWait(driver, 5).until(ec.url_matches(Urls.login_page))

        email = driver.find_element(*Locators.EMAIL_LOGINPAGE_INPUT)
        email.send_keys(User.test_email)

        password = driver.find_element(*Locators.PASSWORD_LOGINPAGE_INPUT)
        password.send_keys(User.test_password)

        driver.find_element(*Locators.GO_BUTTON).click()
        assert WebDriverWait(driver, 5).until(ec.url_matches(Urls.main_page))

    def test_login_button_login_page(self, driver):
        driver.get(Urls.login_page)
        email = driver.find_element(*Locators.EMAIL_LOGINPAGE_INPUT)
        email.send_keys(User.test_email)

        password = driver.find_element(*Locators.PASSWORD_LOGINPAGE_INPUT)
        password.send_keys(User.test_password)

        driver.find_element(*Locators.GO_BUTTON).click()
        assert WebDriverWait(driver, 2).until(ec.url_matches(Urls.main_page))

    def test_login_password_recovery_page(self, driver):
        driver.get(Urls.forgot_password_page)
        driver.find_element(*Locators.SIGN_UP_LINK).click()
        WebDriverWait(driver, 2).until(ec.url_matches(Urls.login_page))

        email = driver.find_element(*Locators.EMAIL_LOGINPAGE_INPUT)
        email.send_keys(User.test_email)

        password = driver.find_element(*Locators.PASSWORD_LOGINPAGE_INPUT)
        password.send_keys(User.test_password)

        driver.find_element(*Locators.GO_BUTTON).click()
        assert WebDriverWait(driver, 2).until(ec.url_matches(Urls.main_page))

    def test_login_register_page(self, driver):
        driver.get(Urls.register_page)
        driver.find_element(*Locators.SIGN_UP_LINK).click()
        WebDriverWait(driver, 2).until(ec.url_matches(Urls.login_page))

        email = driver.find_element(*Locators.EMAIL_LOGINPAGE_INPUT)
        email.send_keys(User.test_email)

        password = driver.find_element(*Locators.PASSWORD_LOGINPAGE_INPUT)
        password.send_keys(User.test_password)

        driver.find_element(*Locators.GO_BUTTON).click()
        assert WebDriverWait(driver, 5).until(ec.url_matches(Urls.main_page))