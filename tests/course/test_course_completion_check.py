import allure
import pytest
from pages.course_page import CourseCompletion
from time import sleep
import pytest_order

@allure.title('Test course completion')
@allure.description('Проверка сохранение того что курс пройден')
@allure.tag('Course', 'Completion')
@allure.epic('Course')
@allure.feature('Completion')
@allure.story('Completion check')
@pytest.mark.order(29)
def test_complete_course(browser):
    complete_course = CourseCompletion(browser)

    complete_course.open()
    complete_course.check_course_completion()

    browser.quit()