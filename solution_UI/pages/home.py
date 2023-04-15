from selenium.webdriver.common.by import By
from lib import helpers
from conftest import logger


logo = (By.ID, "header_logo")
btn_login = (By.XPATH, "//a[@class='login']")
btn_logout = (By.XPATH, "//a[@class='logout']")
btn_account = (By.XPATH, "//a[@class='account']/span")
btn_contact_us = (By.XPATH, "//div[@id='contact-link']/a")

btn_dresses_category = (By.XPATH, "//ul[contains(@class,'menu-content')]/li/a[@title='Dresses']")

_product_xpath = "//div[@class='product-container']/div[@class='right-block']"
lbl_product_names = (By.XPATH, f"{_product_xpath}/h5/a")
lbl_product_prices = (By.XPATH, f"{_product_xpath}//span[@itemprop='price']")

msg_myaccount = (By.XPATH, "//p[@class = 'info-account']")


def click_sign_in(driver):
    logger("Sign in")
    helpers.find_and_click(driver, btn_login)
    helpers.wait_for_page("controller=authentication")


def click_sign_out(driver):
    logger("Logout")
    helpers.find_and_click(driver, btn_logout)
    helpers.find(driver, btn_login)


def click_contact_us(driver):
    logger("Go to 'Contact us' page")
    helpers.find_and_click(driver, btn_contact_us)
    helpers.wait_for_page(driver, "controller=contact")


def click_dresses_tab(driver):
    logger("Go to 'Dresses' page")
    helpers.find_and_click(driver, btn_dresses_category)
    helpers.wait_for_page(driver, "id_category=8")


def get_product_names_and_prices(driver):
    result = helpers.find_all(driver, lbl_product_names)
    if result:
        logger(f"Found {len(result)} products:")
        names = [i.text for i in result]
        prices = [i.text for i in helpers.find_all(driver, lbl_product_prices)]
        courses = dict(zip(names, prices))
        logger(courses)
    else:
        print("Products not found!")