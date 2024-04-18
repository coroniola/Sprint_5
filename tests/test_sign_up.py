from locators import Locators
from settings import Urls
from data import User
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import pytest

class TestSignUP:
    @pytest.mark.usefixtures('driver')
    def test_sign_up_correct_pwd(self, driver):
        driver.get(Urls.register_page)

        name = driver.find_element(*Locators.NAME_REG_PAGE_INPUT)
        name.send_keys(User.test_name)

        email = driver.find_element(*Locators.EMAIL_LOGINPAGE_INPUT)
        email.send_keys(User.test_rand_email)

        password = driver.find_element(*Locators.PASSWORD_LOGINPAGE_INPUT)
        password.send_keys(User.test_rand_password)

        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        assert WebDriverWait(driver, 5).until(ec.url_matches(Urls.login_page))

    def test_sign_up_incorrect_pwd(self, driver):
        driver.get(Urls.register_page)

        name = driver.find_element(*Locators.NAME_REG_PAGE_INPUT)
        name.send_keys(User.test_name)

        email = driver.find_element(*Locators.EMAIL_LOGINPAGE_INPUT)
        email.send_keys(User.test_email)

        password = driver.find_element(*Locators.PASSWORD_LOGINPAGE_INPUT)
        password.send_keys(User.wrong_password)

        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        assert driver.find_element(*Locators.INCORRECT_PASSWORD_MESSAGE).text == "Некорректный пароль"
