import allure
import pytest
from pages.course_page import CourseCompletion
from time import sleep
import pytest_order

@pytest.mark.skip
@pytest.mark.order(21)
def test_complete_course(browser):
    complete_course = CourseCompletion(browser)

    complete_course.open()
    complete_course.check_course_completion()
    browser.quit()