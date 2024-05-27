import allure
from pages.general_page import CheckReviewSort
import pytest
import pytest_order
from time import sleep


@allure.title('Test review sort by')
@allure.description('Отзывы курса сортируются успешно')
@allure.tag('Review', 'SortBy')
@allure.epic('General')
@allure.feature('Reviews')
@allure.story('Sort by helpful')
@pytest.mark.order(7)
def test_check_reviews_sort_hlp(browser):
    check_reviews_sort_hlp = CheckReviewSort(browser)

    check_reviews_sort_hlp.opens()
    check_reviews_sort_hlp.searches()
    check_reviews_sort_hlp.open_random_course()

    check_reviews_sort_hlp.more_reviews()
    check_reviews_sort_hlp.click_more_reviews2()

    check_reviews_sort_hlp.assert_review1()
    check_reviews_sort_hlp.assert_review2()
    sleep(3)
    check_reviews_sort_hlp.compare_reviews()

    browser.quit()