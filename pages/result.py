"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""
from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:

    # Locators

    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result-extras-url-link')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    MORE_RESULTS = (By.ID, 'more-results')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
        
    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles
    
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value
    
    def title(self):
        return self.browser.title
    
    def click_on_more_results(self):
        more_results = self.browser.find_element(*self.MORE_RESULTS)
        more_results.click()
