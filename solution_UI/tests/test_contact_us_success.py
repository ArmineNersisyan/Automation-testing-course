from lib import helpers
from testdata import test_data
from pages import home, sign_in, sign_up, contact_us
from conftest import logger




def test_contact_us_success(driver, message="Some message to support"):
    logger("---test_contact_us_success starts---")
    helpers.go_to_page(driver, test_data.main_url)
    sign_in.login(driver, test_data.email_data, test_data.pass_data)
    allert_text = contact_us.send_message_to_support(driver, message)
    assert allert_text == "Your message has been successfully sent to our team."\
        ,logger("message is incorrect.", error=True)

