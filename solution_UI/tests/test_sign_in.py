from lib import helpers
from testdata import test_data
from pages import sign_in
from conftest import logger



def test_sign_in(driver):
    helpers.go_to_page(driver, test_data.main_url)
    logger("test_sign_in starts!") 
    sign_in.login(driver, test_data.email_data, test_data.pass_data)
    logger("test_sign_in is ended!") 


