from pages.search_page import FilterCheck
import pytest
from time import sleep
import allure


@allure.title('Test search course')
@allure.description('Поиск определенного курса по установленным параметрам')
@allure.tag('Course', 'Search', 'Filter')
@allure.epic('Course')
@allure.feature('Search')
@allure.story('Search and Filter')
@pytest.mark.order(21)
def test_filter(browser):
    filter_check = FilterCheck(browser)

    filter_check.open2()
    filter_check.type_text()
    filter_check.search()

    filter_check.lang_click()
    filter_check.subj_click()
    filter_check.edu_click()
    filter_check.subs_click()
    filter_check.skills_click()
    filter_check.lvl_click()
    filter_check.prod_click()
    filter_check.dur_click()

    browser.quit()
