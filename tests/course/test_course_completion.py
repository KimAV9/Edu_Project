import allure
import pytest
from pages.course_page import CompleteCourse
from time import sleep
import pytest_order

@pytest.mark.skip
@allure.title('Test course completion')
@allure.description('Пройти полностью курс')
@allure.tag('Course', 'Completion')
@allure.epic('Course')
@allure.feature('Completion')
@allure.story('Complete')
@allure.severity('High')
@pytest.mark.order(27)
def test_complete_course(browser):
    complete_course = CompleteCourse(browser)

    complete_course.open()
    complete_course.open_course()

    complete_course.watch_intro()
    complete_course.close_timezone()
    complete_course.click_next()

    complete_course.click_read1()
    complete_course.click_complete()
    complete_course.click_read2()
    complete_course.click_complete()

    complete_course.click_lab()
    complete_course.click_open_lab()
    complete_course.click_open_task()

    complete_course.press_cont()
    complete_course.click_quiz()
    complete_course.click_start_quiz()
    complete_course.answer_quiz()

    complete_course.click_i_understand()
    complete_course.write_name()

    complete_course.submit_quiz()

    browser.quit()
