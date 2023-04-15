from lib import helpers
from testdata import test_data
from pages import practice_page, sign_in_page, sign_up_page, courses_page


def test_pom_workshop():
    helpers.go_to_page(test_data.practice_url)
    # register new user
    practice_page.click_sign_in_btn()
    sign_in_page.click_sign_up_btn()
    login, password = sign_up_page.registration()
    # logout
    practice_page.click_logout_btn()
    # login
    sign_in_page.sign_in(login, password)
    # search courses
    practice_page.click_all_courses_btn()
    courses_page.search_course("Selenium")

    helpers.driver.quit()


if __name__ == '__main__':
    test_pom_workshop()
