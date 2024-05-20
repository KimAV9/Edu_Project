import allure
import pytest
from pages.community_page import TestTags
from pages.community_page import AskQuestion
from time import sleep
import pytest_order


def test_tags(browser):
    test_tag = TestTags(browser)

    test_tag.open_page()
    test_tag.click_featured()
    test_tag.find_tag()
    test_tag.click_tag()
    #print("hi"+test_tag.click_tag().text)



@pytest.mark.skip
def test_question(browser):
    test_questions = AskQuestion(browser)

    test_questions.open_page()
    test_questions.click_featured()
    sleep(5)
    test_questions.click_question()
    # test_questions.write_question()
    test_questions.make_bold()
    test_questions.make_italic()
    test_questions.make_strikethrough()
    test_questions.make_underline()
    test_questions.make_bulletin_list()
    test_questions.write_details()
    # test_questions.click_emoji_menu()
    # test_questions.choose_emoji()
    test_questions.check_text()
