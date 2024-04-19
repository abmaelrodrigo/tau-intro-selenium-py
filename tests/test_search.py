"""
These tests cover DuckDuckGo searches.
"""

import pytest
import unittest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

#@unittest.SkipTest
@pytest.mark.parametrize('phrase', ['selenium'])
def test_basic_duckduckgo_search(browser, phrase):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  

  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for the phrase
  search_page.search(phrase)

  # Then the search result query is the phrase
  assert phrase == result_page.search_input_value()

  # And the search result links pertain to the phrase
  for title in result_page.result_link_titles():
    assert phrase.lower() in title.lower()

  # And the search result title contains the phrase
  # (Putting this assertion last guarantees that the page title will be ready)
  assert phrase in result_page.title()

#@unittest.SkipTest
@pytest.mark.parametrize('phrase', ['pola bear'])
def test_duckduckgo_search_with_click(browser, phrase):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  

  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user types for the phrase
  search_page.type_on_search_bar(phrase)

  # And click on the search button
  search_page.click_on_search_button()

  # Then the search result query is the phrase
  assert phrase == result_page.search_input_value()

  # And the search result links pertain to the phrase
  for title in result_page.result_link_titles():
    assert phrase.lower() in title.lower()

  # And the search result title contains the phrase
  assert phrase in result_page.title()

@pytest.mark.parametrize('phrase', ['pola bear'])
def test_duckduckgo_more_results_button(browser, phrase):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  
 

  # Given the user is on the search result page (the query is the phrase)
  search_page.load()
  search_page.search(phrase)
  assert phrase == result_page.search_input_value()
  

  # When the user clicks on More Results button
  result_page.click_on_more_results()

  # Then the search result links pertain to the phrase
  for title in result_page.result_link_titles():
    assert phrase.lower() in title.lower()

  # And the search result title contains the phrase
  assert phrase in result_page.title()