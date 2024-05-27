import allure
import pytest
from pages.community_page import AskPoll
from time import sleep
import pytest_order


@allure.title('Test create a poll in Community')
@allure.description('Работоспособность создания опросов')
@allure.tag('Community', 'Ask')
@allure.epic('Community')
@allure.feature('Create discussion')
@allure.story('Poll')
@pytest.mark.order(10)
def test_poll(browser):
    ask_poll = AskPoll(browser)

    ask_poll.open_page()
    ask_poll.click_featured()
    ask_poll.log_in()

    ask_poll.click_poll()
    ask_poll.add_option()
    ask_poll.write_question()
    ask_poll.write_options()

    #ask_poll.click_ask()
    browser.quit()
