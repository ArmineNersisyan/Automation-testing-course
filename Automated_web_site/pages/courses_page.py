import time

from selenium.webdriver.common.by import By

from lib import helpers
from lib.test_logger import logger

search_field = (By.XPATH, "//input[@id='search']")
btn_search_course = (By.XPATH, "//button[contains(@class, 'search-course')]")
search_result = (By.XPATH, "//div[@class='zen-course-list']")
search_result_names = (By.XPATH, "//div[@class='zen-course-list']//h4")
search_result_price = (By.XPATH, "//div[@class='zen-course-list']//span[contains(@class,'zen-course-price')]")


def search_course(course_name):
    helpers.find_and_send_keys(search_field, course_name)
    helpers.find_and_click(btn_search_course)
    time.sleep(1.5)
    result = helpers.find_all(search_result)
    if result:
        logger(f"Found {len(result)} '{course_name}' courses:")
        names = [i.text for i in helpers.find_all(search_result_names)]
        prices = [i.text for i in helpers.find_all(search_result_price)]
        courses = dict(zip(names, prices))
        logger(courses)
    else:
        logger("Courses not found!", error=True)

