import allure
import pytest
from pages.profile_page import ProfilePage
from time import sleep
import pytest_order


@allure.story('Change education in profile')
@pytest.mark.skip
def test_education(browser):
    profile_page = ProfilePage(browser)

    profile_page.open2()

    profile_page.p_open_prof_menu()
    profile_page.p_open_profile()
    profile_page.e2_add_edu()
    profile_page.e2_name_of_inst()
    profile_page.e2_choose_inst()
    profile_page.e2_degree()
    profile_page.e2_choose_degree()
    profile_page.e2_discipline()
    profile_page.e2_choose_discipline()
    profile_page.e2_area_of_conc()
    profile_page.e2_start_month()
    profile_page.e2_start_choose_month()
    profile_page.e2_start_year()
    profile_page.e2_start_choose_year()
    profile_page.e2_end_month()
    profile_page.e2_end_choose_month()
    profile_page.e2_end_year()
    profile_page.e2_end_choose_year()
    profile_page.e2_cumulative_grade()
    profile_page.e2_currently_study()
    profile_page.e2_save()
    browser.quit()