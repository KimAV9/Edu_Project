import allure
import pytest
from pages.profile_page import ProfilePage
from time import sleep
import pytest_order


@allure.story('Change personal information in profile')
@pytest.mark.order(5)
@pytest.mark.skip
def test_edit_personal_info(browser):
    profile_page = ProfilePage(browser)

    profile_page.open2()

    profile_page.p_open_prof_menu()
    profile_page.p_open_profile()
    profile_page.ed2_edit()
    profile_page.ed2_name()
    profile_page.ed2_pronouns()
    profile_page.ed2_gender()
    profile_page.ed2_choose_gender()
    profile_page.ed2_save()
    browser.quit()
