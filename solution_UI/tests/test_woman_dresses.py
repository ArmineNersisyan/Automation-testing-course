from lib import helpers
from testdata import test_data
from pages import home
from conftest import logger



def test_woman_dresses(driver):
    logger("test_woman_dresses starts!")
    helpers.go_to_page(driver, test_data.main_url)
    home.click_dresses_tab(driver)
    home.get_product_names_and_prices(driver)
    logger("test_woman_dresses end!")


