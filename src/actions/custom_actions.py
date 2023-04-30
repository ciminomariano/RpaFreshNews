import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.exceptions.custom_exceptions import CustomException
from src.exceptions.selenium_exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class CustomActions:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def open_website(self, url):
        try:
            self.browser.get(url)
            return True
        except NoSuchElementException:
            raise CustomException("We could not find any element at the page")
        except WebDriverException:
            raise CustomException("The page could not be loaded")

    def maximaze_nav(self):
        try:
            self.browser.maximize_window()
            time.sleep(5)
            return True
        except Exception:
            raise CustomException("The Browser could not be Maximized")

    def accept_cookies(self):
        try:
            boton_accept = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[@data-testid="GDPR-accept"]'))
            )
            if boton_accept:
                boton_accept.click()
                print("Accept button Found, clicking on it")
                time.sleep(1)
                return True
        except Exception:
            raise CustomException("The element boton_aceppt from cookies"
                                  "was not found")

    def click_search_bar(self):
        try:
            search_button = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'button[data-test-id="search-button"]')))
            search_button.click()
            time.sleep(5)
            print("Search button found :), clicking on it")
            return True
        except TimeoutException:
            print("Search button not found")

    def write_search_term(self, term):
        try:
            search_input = self.browser.find_element(By.CSS_SELECTOR, 'input[data-testid="search-input"]')
            time.sleep(3)
            search_input.send_keys(term)
            time.sleep(1)
            search_input.send_keys(Keys.ENTER)
            time.sleep(5)
            return True
        except TimeoutException:
            print("Se agotó el tiempo de espera para encontrar la barra para escribir")
