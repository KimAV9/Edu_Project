import allure
import pytest
from pages.profile_page import ProfilePageVisibility
from time import sleep
import pytest_order


@allure.title('Test change visbility in profile')
@allure.description('Изменить статус видимости профиля')
@allure.tag('Account', 'Profile')
@allure.epic('Account')
@allure.feature('Profile')
@allure.story('Visibility')
@pytest.mark.order(14)
def test_visibility_update(browser):
    profile_page_vis = ProfilePageVisibility(browser)

    profile_page_vis.open2()

    profile_page_vis.p_open_prof_menu()
    profile_page_vis.p_open_profile()

    profile_page_vis.v2_udt_vis()
    profile_page_vis.v2_who_sees()
    profile_page_vis.v2_done()

    browser.quit()
