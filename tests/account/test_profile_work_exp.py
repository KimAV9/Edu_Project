import allure
import pytest
from pages.profile_page import ProfilePageWorkExp
from time import sleep
import pytest_order


@allure.title('Test change work expirirence in profile')
@allure.description('Изменение данных в профиле аккаунта о работе')
@allure.tag('Account', 'Profile')
@allure.epic('Account')
@allure.feature('Profile')
@allure.story('Work history')
@pytest.mark.order(15)

def test_work_exp(browser):
    profile_page_wk_exp = ProfilePageWorkExp(browser)

    profile_page_wk_exp.open2()

    profile_page_wk_exp.p_open_prof_menu()
    profile_page_wk_exp.p_open_profile()

    profile_page_wk_exp.w2_add_work_exp()
    profile_page_wk_exp.w2_click_name_of_inst()
    profile_page_wk_exp.w2_choose_name_of_inst()

    profile_page_wk_exp.w2_click_role()
    profile_page_wk_exp.w2_choose_role()

    profile_page_wk_exp.w2_start_month()
    profile_page_wk_exp.w2_start_choose_month()
    profile_page_wk_exp.w2_start_year()
    profile_page_wk_exp.w2_start_choose_year()

    profile_page_wk_exp.w2_end_month()
    profile_page_wk_exp.w2_end_choose_month()
    profile_page_wk_exp.w2_end_year()
    profile_page_wk_exp.w2_end_choose_year()

    profile_page_wk_exp.w2_current_work()
    profile_page_wk_exp.w2_end_date_block()
    profile_page_wk_exp.w2_add_description()

    profile_page_wk_exp.w2_save()
    browser.quit()


