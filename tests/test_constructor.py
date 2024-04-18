from locators import Locators
from settings import Urls
from data import User
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import pytest

class TestConstructor:

    def test_constructor_toppings_section_navigation(self, driver):
        driver.get(Urls.main_page)
        driver.find_element(*Locators.TOPPINGS_SECTION).click()

        assert driver.find_element(*Locators.TOPPINGS_SECTION_H2).text == "Начинки"


    def test_constructor_sauces_section_navigation(self, driver):
        driver.get(Urls.main_page)
        driver.find_element(*Locators.SAUCES_SECTION).click()

        assert driver.find_element(*Locators.SAUCES_SECTION_H2).text == "Соусы"

    def test_constructor_buns_section_navigation(self, driver):
        driver.get(Urls.main_page)
        driver.find_element(*Locators.SAUCES_SECTION).click()
        driver.find_element(*Locators.BUNS_SECTION).click()

        assert driver.find_element(*Locators.BUNS_SECTION_H2).text == "Булки"




