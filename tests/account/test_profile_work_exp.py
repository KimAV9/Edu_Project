import allure
import pytest
from pages.porfile_page import ProfilePage
from time import sleep
import pytest_order


@allure.story('Change work experience in profile')
@pytest.mark.skip
def test_work_exp(browser):
    profile_page = ProfilePage(browser)

    profile_page.open2()

    profile_page.p_open_prof_menu()
    profile_page.p_open_profile()

    profile_page.w2_add_work_exp()
    profile_page.w2_click_name_of_inst()
    profile_page.w2_choose_name_of_inst()
    profile_page.w2_click_role()
    profile_page.w2_choose_role()
    profile_page.w2_start_month()
    profile_page.w2_start_choose_month()
    profile_page.w2_start_year()
    profile_page.w2_start_choose_year()
    profile_page.w2_end_month()
    profile_page.w2_end_choose_month()
    profile_page.w2_end_year()
    profile_page.w2_end_choose_year()
    profile_page.w2_current_work()
    profile_page.w2_end_date_block()
    profile_page.w2_add_description()
    profile_page.w2_save()

    browser.quit()


