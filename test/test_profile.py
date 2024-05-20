import allure
import pytest
from pages.porfile_page import ProfilePage
from time import sleep
import pytest_order


@allure.story('Profile changes check')
@pytest.mark.skip
def test_profile(browser):
    profile_page = ProfilePage(browser)

    profile_page.open2()

    profile_page.p_open_prof_menu()
    profile_page.p_open_profile()

    #rofile_page.w2_add_work_exp()
    #profile_page.w2_click_name_of_inst()
    #profile_page.w2_choose_name_of_inst()
    #profile_page.w2_click_role()
    #profile_page.w2_choose_role()
    #profile_page.w2_start_month()
    #profile_page.w2_start_choose_month()
    #profile_page.w2_start_year()
    #profile_page.w2_start_choose_year()
    #profile_page.w2_end_month()
    #profile_page.w2_end_choose_month()
    #profile_page.w2_end_year()
    #profile_page.w2_end_choose_year()
    #profile_page.w2_current_work()
    #profile_page.w2_end_date_block()
    #profile_page.w2_add_description()
    #profile_page.w2_save()

    #profile_page.e2_add_edu()
    #profile_page.e2_name_of_inst()
    #profile_page.e2_choose_inst()
    #profile_page.e2_degree()
    #profile_page.e2_choose_degree()
    #profile_page.e2_discipline()
    #profile_page.e2_choose_discipline()
    #profile_page.e2_area_of_conc()
    #profile_page.e2_start_month()
    #profile_page.e2_start_choose_month()
    #profile_page.e2_start_year()
    #profile_page.e2_start_choose_year()
    #profile_page.e2_end_month()
    #profile_page.e2_end_choose_month()
    #profile_page.e2_end_year()
    #profile_page.e2_end_choose_year()
    #profile_page.e2_cumulative_grade()
    #profile_page.e2_currently_study()
    #profile_page.e2_save()

    #profile_page.wp2_work_pref()
    #profile_page.wp2_role()
    #profile_page.wp2_choose_role()
    #profile_page.wp2_industry()
    #profile_page.wp2_choose_industry()
    #profile_page.wp2_save()

    #profile_page.i2_add_info()
    #profile_page.i2_write_about()
    #profile_page.i2_save()

    profile_page.v2_udt_vis()
    profile_page.v2_who_sees()
    profile_page.v2_done()

    profile_page.ed2_edit()
    profile_page.ed2_name()
    profile_page.ed2_pronouns()
    profile_page.ed2_gender()
    profile_page.ed2_choose_gender()
    profile_page.ed2_save()
    sleep(10)
