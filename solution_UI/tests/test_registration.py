from lib import helpers
from testdata import test_data
from pages import home, sign_up
from conftest import logger




def test_registration(driver):
    logger("---test_1_registration starts---")
    helpers.go_to_page(driver, test_data.main_url)
    sign_up.create_new_account(driver)
    assert helpers.find(driver, home.msg_myaccount, get_text=True)==test_data.msg_myaccount\
           ,logger("Registration failed!", error=True)
    logger("Registration success!")


