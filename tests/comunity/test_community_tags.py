import allure
import pytest
from pages.community_page import TagsTesting
from time import sleep
import pytest_order

@pytest.mark.skip
@pytest.mark.order(11)
def test_tags(browser):
    test_tag = TagsTesting(browser)

    test_tag.open_page()
    test_tag.click_featured()
    sleep(5)
    test_tag.find_tag()
    test_tag.check_tag_to_click()
    test_tag.click_tag()
    sleep(5)
    test_tag.find_disc_tags()
    test_tag.check_tags()
    browser.quit()


