from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from lib import helpers
from lib.test_logger import logger

title = (By.XPATH, "//title[text()='Practice Page']")
btn_alert = (By.ID, "alertbtn")
btn_hide = (By.ID, "hide-textbox")
inp_example = (By.ID, "displayed-text")
btn_mousehover = (By.ID, 'mousehover')
btn_top = (By.XPATH, "//button[@id='mousehover']//following::a[text()='Top']")
footer = (By.XPATH, "//div[contains(@class, 'footer')]//p")
page_body = (By.TAG_NAME, 'body')

btn_all_courses = (By.XPATH, "//a[contains(text(),'ALL COURSES')]")
btn_sign_in = (By.XPATH, "//a[@href='/login']")
btn_dropdown_menu = (By.XPATH, "//button[@id='dropdownMenu1']")
btn_logout = (By.XPATH, "//div[@class='dropdown open']//a[contains(text(),'Logout')]")


def save_alert_text():
    helpers.find_and_click(btn_alert)
    alert = helpers.switch_to_alert()
    logger(f'Alert text is - {alert.text}')
    alert.accept()


def hide_element_check():
    helpers.find_and_click(btn_hide)
    hide_attr = helpers.find(inp_example, get_attribute='style')
    logger(f'Hidden attribute is - {hide_attr}')


def mouse_hover_check():
    helpers.find_and_click(btn_mousehover)
    helpers.find_and_click(btn_top)


def footer_text():
    f_text = helpers.find(footer, get_text=True)
    logger(f'Footer text is - {f_text}')


def click_sign_in_btn():
    helpers.find_and_send_keys(page_body, (Keys.CONTROL + Keys.HOME))
    helpers.find_and_click(btn_sign_in)
    helpers.wait_for_page("/login")


def click_logout_btn():
    logger("Logout")
    helpers.find_and_click(btn_dropdown_menu)
    helpers.find_and_click(btn_logout)
    helpers.find(btn_sign_in)


def click_all_courses_btn():
    logger("Navigate to 'All courses' page")
    helpers.find_and_send_keys(page_body, (Keys.CONTROL + Keys.HOME))
    helpers.find_and_click(btn_all_courses)
    helpers.wait_for_page("/courses")
