import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.exceptions.custom_exceptions import CustomException, log_section_not_found
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
            print("Time expired to find search input bar")

    def apply_categories(self, news_categories):
        try:
            section_button = self.browser.find_element(By.XPATH, '//button[@data-testid="search-multiselect-button"]')
            section_button.click()
            time.sleep(5)
            print("Section button clicked")


            categories_xpath = {
                "arts" :'//input[@type="checkbox" and @data-testid="DropdownLabelCheckbox" and @value="Arts|nyt://section/6e6ee292-b4bd-5006-a619-9ceab03524f2"]',
                "books": '//input[@type="checkbox" and @data-testid="DropdownLabelCheckbox" and @value="Books|nyt://section/550f75e2-fc37-5d5c-9dd1-c665ac221b49"]',
                "business": '//input[@type="checkbox" and @value="Business|nyt://section/0415b2b0-513a-5e78-80da-21ab770cb753"]',
                "movies": '//input[@type="checkbox" and @data-testid="DropdownLabelCheckbox" and @value="Movies|nyt://section/62b3d471-4ae5-5ac2-836f-cb7ad531c4cb"]',
                "new york": '//input[@value="New York|nyt://section/39480374-66d3-5603-9ce1-58cfa12988e2"]',
                "opinion": '//input[@type="checkbox" and @data-testid="DropdownLabelCheckbox" and @value="Opinion|nyt://section/d7a71185-aa60-5635-bce0-5fab76c7c297"]',
                "sports": '//input[@value="Sports|nyt://section/4381411b-670f-5459-8277-b181485a19ec"]',
                "style": '//input[@data-testid="DropdownLabelCheckbox" and @value="Style|nyt://section/146e2c45-6586-59ef-bc23-90e88fe2cf0a"]',
                "magazine": '//input[@type="checkbox" and @data-testid="DropdownLabelCheckbox" and @value="Magazine|nyt://section/a913d1fb-3cdf-556b-9a81-f0b996a1a202"]',
                "U.S": "//input[@data-testid='DropdownLabelCheckbox' and @value='U.S.']",
                "technology": '//input[@value="Technology|nyt://section/4224240f-b1ab-50bd-881f-782d6a3bc527"]',
                "WORLD": "//input[@data-testid='DropdownLabelCheckbox' and @value='World']",
            }

            for category in news_categories:

                xpath = categories_xpath.get(category.lower())

                if category == "ARTS":
                    try:
                        business_category = self.browser.find_element(By.XPATH, xpath)
                        business_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "BOOKS":
                    try:
                        any_checkbox = self.browser.find_element(By.XPATH, xpath)
                        any_checkbox.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "BUSINESS":
                    try:
                        business_category = self.browser.find_element(By.XPATH, xpath)
                        business_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "MOVIES":
                    try:
                        business_category = self.browser.find_element(By.XPATH, xpath)
                        business_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "NEW YORK":
                    try:
                        new_york_category = self.browser.find_element(By.XPATH,xpath)
                        new_york_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "OPINION":
                    try:
                        new_york_category = self.browser.find_element(By.XPATH,xpath)
                        new_york_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "SPORTS":
                    try:
                        sports_category = self.browser.find_element(By.XPATH,xpath)
                        sports_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "STYLE":
                    try:
                        style_category = self.browser.find_element(By.XPATH,xpath)
                        style_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "MAGAZINE":
                    try:
                        magazine_category = self.browser.find_element(By.XPATH,xpath)
                        magazine_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "U.S":
                    try:
                        opinion_category = self.browser.find_element(By.XPATH,xpath)
                        opinion_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "TECHNOLOGY":
                    try:
                        technology_category = self.browser.find_element(By.XPATH,xpath)
                        technology_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

                elif category == "WORLD":
                    try:
                        technology_category = self.browser.find_element(By.XPATH,xpath)
                        technology_category.click()
                        time.sleep(2)
                    except Exception as e:
                        log_section_not_found(category, e)

        except TimeoutException:
            print("Time expired to find the button ")
