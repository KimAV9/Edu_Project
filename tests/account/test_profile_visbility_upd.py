import allure
import pytest
from pages.porfile_page import ProfilePage
from time import sleep
import pytest_order


@allure.story('Change visibility in profile')
@pytest.mark.skip
def test_visibility_update(browser):
    profile_page = ProfilePage(browser)

    profile_page.open2()

    profile_page.p_open_prof_menu()
    profile_page.p_open_profile()

    profile_page.v2_udt_vis()
    profile_page.v2_who_sees()
    profile_page.v2_done()

    browser.quit()
