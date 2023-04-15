from lib import helpers
from testdata import test_data
from pages import  sign_in, contact_us
from conftest import logger



def test_contact_us_error(driver):
        logger("---test_contact_us_success starts---")
        helpers.go_to_page(driver,test_data.main_url)
        sign_in.login(driver, test_data.email_data, test_data.pass_data)
        allert_text = contact_us.send_message_to_support(driver)
        assert allert_text == "The message cannot be blank."\
            ,logger("message is incorrect.", error=True)
        logger("---test_contact_us_error ends---")


if __name__ == '__main__':
    test_contact_us_error(driver)