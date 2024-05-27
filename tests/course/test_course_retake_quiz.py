import allure
import pytest
from pages.course_page import RetakeTest
from time import sleep
import pytest_order

@pytest.mark.skip
@allure.title('Test retake quiz')
@allure.description('Пересдать тест')
@allure.tag('Course', 'Completion')
@allure.epic('Course')
@allure.feature('Completion')
@allure.story('Quiz Retake')
@pytest.mark.order(28)
def test_retake_test(browser):
    retake_test = RetakeTest(browser)

    retake_test.open()
    retake_test.open_course()
    retake_test.open_test_page()

    retake_test.click_continue()
    retake_test.click_try_again()
    retake_test.check_if_capable()

    retake_test.answer_quiz()
    retake_test.click_i_understand()
    retake_test.write_name()
    retake_test.submit_quiz()

    browser.quit()