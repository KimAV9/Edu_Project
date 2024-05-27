import allure
import pytest
from pages.profile_page import ProfilePageWorkPref
from time import sleep
import pytest_order


@allure.title('Test change work preferences in profile')
@allure.description('Изменение данных в профиле аккаунта об предпочтения о работе')
@allure.tag('Account', 'Profile')
@allure.epic('Account')
@allure.feature('Profile')
@allure.story('Work preferences')
@allure.severity('High')
@pytest.mark.order(16)
def test_work_pref(browser):
    profile_page_wk_pref = ProfilePageWorkPref(browser)

    profile_page_wk_pref.open2()

    profile_page_wk_pref.p_open_prof_menu()
    profile_page_wk_pref.p_open_profile()

    profile_page_wk_pref.wp2_work_pref()

    profile_page_wk_pref.wp2_role()
    profile_page_wk_pref.wp2_choose_role()
    profile_page_wk_pref.wp2_industry()
    profile_page_wk_pref.wp2_choose_industry()

    profile_page_wk_pref.wp2_save()
    browser.quit()
