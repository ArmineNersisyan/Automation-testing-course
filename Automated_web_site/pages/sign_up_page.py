from selenium.webdriver.common.by import By
from lib import helpers
from lib.test_logger import logger

txt_name = (By.ID, "name")
txt_last_name = (By.ID, "last_name")
txt_email = (By.ID, "email")
txt_pass = (By.ID, "password")
txt_pass_confirm = (By.ID, "password_confirmation")
btn_sign_up_confirm = (By.XPATH, "//input[@value='Sign Up']")
msg_invalid = (By.XPATH, "//input[@id='email']//following::span[contains(text(),'invalid')]")
btn_sign_up = (By.XPATH, "//a[@href='/register']")


def registration():
    login = f"{helpers.random_string(10)}@{helpers.random_string(5)}.com"
    password = helpers.random_string(6)
    logger(f"Register new user: {login} : {password}")
    helpers.find_and_send_keys(txt_name, helpers.random_string(5))
    helpers.find_and_send_keys(txt_last_name, helpers.random_string(5))
    helpers.find_and_send_keys(txt_email, login)
    helpers.find_and_send_keys(txt_pass, password)
    helpers.find_and_send_keys(txt_pass_confirm, password)
    helpers.find_and_click(btn_sign_up_confirm)
    helpers.wait_for_page(not_page="/register")
    return login, password
