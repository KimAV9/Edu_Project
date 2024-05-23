import allure
import pytest
from pages.profile_page import ProfilePage
from time import sleep
import pytest_order


@allure.story('Change work preferences in profile')
@pytest.mark.order(3)
@pytest.mark.skip
def test_work_pref(browser):
    profile_page = ProfilePage(browser)

    profile_page.open2()

    profile_page.p_open_prof_menu()
    profile_page.p_open_profile()
    profile_page.wp2_work_pref()
    profile_page.wp2_role()
    profile_page.wp2_choose_role()
    profile_page.wp2_industry()
    profile_page.wp2_choose_industry()
    profile_page.wp2_save()

    browser.quit()
