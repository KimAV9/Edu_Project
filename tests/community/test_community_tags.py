import allure
import pytest
from pages.community_page import TagsTesting
from time import sleep
import pytest_order


@allure.title('Test search by tags in community')
@allure.description('Поиск определённых тем используя предоставленные тэги')
@allure.tag('Community', 'Ask')
@allure.epic('Community')
@allure.feature('Search')
@allure.story('Tag')
@allure.severity('Normal')
@pytest.mark.order(8)
def test_tags(browser):
    test_tag = TagsTesting(browser)

    test_tag.open_page()
    test_tag.click_featured()

    test_tag.find_tag()
    test_tag.check_tag_to_click()
    test_tag.click_tag()

    test_tag.find_disc_tags()
    test_tag.check_tags()
    browser.quit()
