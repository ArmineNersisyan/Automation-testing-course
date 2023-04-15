import time
from selenium.webdriver.common.by import By
from lib import helpers
from lib.test_logger import logger
from pages.practice_page import click_sign_in_btn
from testdata import test_data

btn_sign_in = (By.XPATH, "//a[@href='/login']")
txt_email = (By.ID, "email")
txt_pass = (By.ID, "password")
btn_login = (By.XPATH, "//input[@value='Login']")
msg_invalid = (By.XPATH, "//input[@id='email']//following::span[contains(text(),'invalid')]")
btn_sign_up = (By.XPATH, "//a[@href='/register']")


def sign_in(email="", password="", expected_error=False):
    email = email if email else test_data.email_data
    password = password if password else test_data.pass_data
    logger(f"Login with user: {email} : {password}")
    click_sign_in_btn()
    helpers.find_and_send_keys(txt_email, email)
    helpers.find_and_send_keys(txt_pass, password)
    time.sleep(5)
    helpers.find_and_click(btn_login)
    if expected_error:
        validation_msg = helpers.find(msg_invalid, 5, get_text=True)
        logger(f'Validation Message is - {validation_msg}')
    else:
        helpers.wait_element_disappear(btn_sign_in)


def click_sign_up_btn():
    helpers.find_and_click(btn_sign_up)
    helpers.wait_for_page("/register")
