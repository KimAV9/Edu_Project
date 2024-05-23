import allure
from pages.general_page import CheckReviewSort
import pytest
import pytest_order
from time import sleep


@pytest.mark.skip
def test_check_reviews_sort_hlp(browser):
    check_reviews_sort_hlp = CheckReviewSort(browser)

    check_reviews_sort_hlp.temp_open()
    check_reviews_sort_hlp.click_more_reviews()
    check_reviews_sort_hlp.assert_review1()
    check_reviews_sort_hlp.assert_review2()
    sleep(5)
    check_reviews_sort_hlp.compare_reviews()

    browser.quit()