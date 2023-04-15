from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from lib import helpers
from pages import home
from conftest import logger


txt_new_email = (By.ID, "email_create")
btn_create_account = (By.ID, "SubmitCreate")
txt_first_name = (By.ID, "customer_firstname")
txt_last_name = (By.ID, "customer_lastname")
txt_email = (By.ID, "email")
txt_pass = (By.ID, "passwd")
txt_address1 = (By.ID, "address1")
txt_city = (By.ID, "city")
dd_state = (By.XPATH, "//select[@id='id_state']")
txt_post_code = (By.ID, "postcode")
txt_mobile = (By.ID, "phone_mobile")
btn_submit_registration = (By.ID, "submitAccount")


def create_new_account(driver, new_email="", new_pass=""):
    new_email = new_email if new_email else f"{helpers.random_string(10)}@{helpers.random_string(5)}.com"
    new_pass = new_pass if new_pass else helpers.random_string(10)
    home.click_sign_in(driver)
    logger(f"Create new account: [{new_email}: {new_pass}]")
    helpers.find_and_send_keys(driver, txt_new_email, new_email)
    helpers.find_and_click(driver, btn_create_account)
    helpers.wait_for_page(driver, "#account-creation")

    helpers.find_and_send_keys(driver, txt_first_name, "first")
    helpers.find_and_send_keys(driver, txt_last_name, "last")
    helpers.find_and_click(driver, txt_email)
    helpers.find_and_send_keys(driver, txt_pass, new_pass)
    helpers.find_and_send_keys(driver, txt_address1, "Some Address")
    helpers.find_and_send_keys(driver, txt_city, "Some City")
    Select(helpers.find(driver, dd_state)).select_by_index(1)
    helpers.find_and_send_keys(driver, txt_post_code, "12345")
    helpers.find_and_send_keys(driver, txt_mobile, "987654321")
    helpers.find_and_click(driver, btn_submit_registration)

    helpers.wait_for_page(driver, "controller=my-account")
    helpers.find(driver, home.btn_account)
    logger("Account created successfully!")
    return new_email, new_pass
