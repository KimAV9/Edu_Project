import allure
import pytest
from pages.porfile_page import ProfilePage
from time import sleep
import pytest_order


@allure.story('Change additional in profile')
@pytest.mark.skip
def test_additional_info(browser):
    profile_page = ProfilePage(browser)

    profile_page.open2()

    profile_page.p_open_prof_menu()
    profile_page.p_open_profile()

    profile_page.i2_add_info()
    profile_page.i2_write_about()
    profile_page.i2_save()

    browser.quit()
