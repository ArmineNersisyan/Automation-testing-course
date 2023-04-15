from selenium.webdriver.common.by import By
from lib import helpers
from pages import home
from testdata import test_data
from conftest import logger


txt_email = (By.ID, "email")
txt_pass = (By.ID, "passwd")
btn_login = (By.XPATH, "//button[@id='SubmitLogin']")


def login(driver, email="", password=""):
    email = email if email else test_data.email_data
    password = password if password else test_data.pass_data
    home.click_sign_in(driver)
    logger(f"Login with user: [{email} : {password}]")
    helpers.find_and_send_keys(driver, txt_email, email)
    helpers.find_and_send_keys(driver, txt_pass, password)
    helpers.find_and_click(driver, btn_login)
    helpers.wait_for_page(driver, "controller=my-account")
    helpers.find(driver, home.btn_account)
