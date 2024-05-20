import allure
import pytest
from pages.community_page import TestTags
from time import sleep
import pytest_order


def test_tags(browser):
    test_tags = TestTags(browser)

    test_tags.open_page()
    test_tags.click_featured()
    test_tags.click_tag()
