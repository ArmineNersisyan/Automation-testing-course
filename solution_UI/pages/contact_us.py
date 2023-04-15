import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from lib import helpers
from pages import home
from testdata import test_data
from conftest import logger


dd_subject = (By.ID, "id_contact")
dd_reference = (By.XPATH, "//select[@name='id_order']")
field_attach_file = (By.ID, "fileUpload")
txt_message = (By.ID, "message")
btn_send_message = (By.ID, "submitMessage")
alert_success = (By.XPATH, "//p[contains(@class,'alert-success')]")
alert_fail = (By.XPATH, "//div[contains(@class,'alert-danger')]//li")


def send_message_to_support(driver, message=""):
    home.click_contact_us(driver)
    logger(f"Send message to support: '{message}'")
    Select(helpers.find(driver, dd_subject)).select_by_index(1)
    driver.find_element(*field_attach_file).send_keys(f"{os.getcwd()}/{test_data.log_file_name}")
    helpers.find_and_send_keys(driver, txt_message, message) if message else None
    helpers.find_and_click(driver, btn_send_message)
    alert_text = helpers.find(driver, alert_success if message else alert_fail, get_text=True)
    return alert_text

