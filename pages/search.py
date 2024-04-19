"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:

    
    # URL
    URL = 'https://www.duckduckgo.com'

    # Locators
    SEARCH_INPUT = (By.ID, 'searchbox_input')
    SEARCH_BUTTON = (By.CLASS_NAME, 'searchbox_searchButton__F5Bwq')

    # Initializer
    def __init__(self, browser):
        self.browser = browser
        
    # Interaction Methods
    def load(self):
        """
        The driver.get method will navigate 
        to a page given by the URL. WebDriver will wait 
        until the page has fully loaded 
        """
        self.browser.get(self.URL)

    def search(self,phrase):
        """
        The * operator to expand the SEARCH_INPUT locator tuple into arguments
        """
        search_input = self.browser.find_element(*self.SEARCH_INPUT)

        """
        The addition of Keys.RETURN will send the ENTER/RETURN key as well
        """
        search_input.send_keys(phrase + Keys.RETURN)

    def type_on_search_bar(self,phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
    
    def click_on_search_button(self):
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()

