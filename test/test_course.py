import allure
import pytest
from pages.course_page import CoursePage
from time import sleep
import pytest_order

@pytest.mark.skip
def test_complete_course(browser):
    complete_course = CoursePage(browser)

    complete_course.open()
    complete_course.search_course()
    complete_course.click_search()
    complete_course.click_course()

    complete_course.enroll()
    #complete_course.click_continue()
    #complete_course.close_commit_window()
    #complete_course.close_goals_window()

    complete_course.watch_intro()
    #complete_course.click_read1()
    #complete_course.click_complete()
    #complete_course.click_read2()
    #complete_course.click_complete()

    #complete_course.click_lab()
    #complete_course.click_open_lab()
    #complete_course.click_open_task()

    complete_course.click_quiz()
    complete_course.click_start_quiz()
    complete_course.answer_quiz()
    complete_course.click_i_understand()
    complete_course.submit_quiz()
