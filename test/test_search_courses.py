from pages.search_page import FilterCheck
import pytest
from time import sleep


def test_filter(browser):
    filter_check = FilterCheck(browser)

    filter_check.open2()
    filter_check.login2()
    sleep(15)
    filter_check.search()

    filter_check.subj()
    filter_check.subj_click()
    filter_check.lang_click()
    filter_check.prod_click()
    filter_check.lvl_click()
    filter_check.dur_click()
    filter_check.skills_click()
    filter_check.subs_click()
    filter_check.edu_click()
