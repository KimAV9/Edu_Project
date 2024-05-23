import allure
import pytest
from pages.course_page import EnrollToCourse
from time import sleep
import pytest_order

@pytest.mark.skip
@pytest.mark.order(14)
def test_enroll_to_course(browser):
    enroll_to_course = EnrollToCourse(browser)

    enroll_to_course.open()
    enroll_to_course.search_course()
    enroll_to_course.click_search()
    enroll_to_course.click_course()

    enroll_to_course.enroll()
    enroll_to_course.click_continue()
    enroll_to_course.close_commit_window()
    enroll_to_course.close_goals_window()
    browser.quit()
