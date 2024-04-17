"""
These tests cover DuckDuckGo searches.
"""

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

def test_basic_duckduckgo_search(browser):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  PHRASE = "Selenium"

  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for "Selenium"
  search_page.search(PHRASE)

  # Then the search result title contains "Selenium"
  assert PHRASE in result_page.title()

  # And the search result query is "Selenium"
  assert PHRASE == result_page.serach_input_value()

  # And the search result links pertain to "Selenium"
  for title in result_page.result_link_titles():
    assert PHRASE.lower() in title.lower()

  raise Exception("Incomplete Test")