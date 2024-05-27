import allure
import pytest
from pages.profile_page import ProfilePageDeleteData
from time import sleep
import pytest_order


@allure.title('Test delete data in profile')
@allure.description('Удаление данных из профиля аккаунта такие как work history, education, work preference')
@allure.tag('Account', 'Profile')
@allure.epic('Account')
@allure.feature('Profile')
@allure.story('Deletion')
@pytest.mark.order(17)
def test_delete_personal_data(browser):
    profile_page = ProfilePageDeleteData(browser)

    profile_page.open2()

    profile_page.p_open_prof_menu()
    profile_page.p_open_profile()

    profile_page.click_edit_work_exp()
    profile_page.remove_work_exp()
    sleep(1)

    profile_page.click_edit_edu()
    profile_page.remove_edu()
    sleep(1)

    profile_page.click_edit_wk_pref()
    profile_page.remove_wk_pref()
    profile_page.save_wk_pref()

    browser.quit()
