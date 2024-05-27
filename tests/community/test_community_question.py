import allure
import pytest
from pages.community_page import AskQuestion
from time import sleep
import pytest_order


@allure.title('Test create a question in Community')
@allure.description('Работоспособность функционала создания вопросов')
@allure.tag('Community', 'Ask')
@allure.epic('Community')
@allure.feature('Create discussion')
@allure.story('Question')
@allure.severity('Normal')
@pytest.mark.order(9)
def test_question(browser):
    test_questions = AskQuestion(browser)

    test_questions.open_page()
    test_questions.click_featured()
    test_questions.log_in()
    test_questions.click_question()

    test_questions.write_question()
    test_questions.make_bold()
    test_questions.make_italic()
    test_questions.make_strikethrough()
    test_questions.make_underline()
    test_questions.make_bulletin_list()
    test_questions.write_details()

    test_questions.check_text()
    browser.quit()
