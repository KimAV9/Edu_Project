import allure
import pytest
from pages.course_page import RateCourse
from time import sleep
import pytest_order

@pytest.mark.skip
def test_complete_course(browser):
    rate_course = RateCourse(browser)

    rate_course.open()
    rate_course.open_menu()
    rate_course.click_rate()
    rate_course.rate_course()
    #rate_course.submit_rating()
    browser.quit()