import allure
import pytest
from pages.profile_page import ProfilePagePersInfo
from time import sleep
import pytest_order


@allure.title('Test change personal information in profile')
@allure.description('Изменить и сохранить данные в профиле по о имени, полу и метоимениям')
@allure.tag('Account', 'Profile')
@allure.epic('Account')
@allure.feature('Profile')
@allure.story('Personal info')
@pytest.mark.order(13)
def test_edit_personal_info(browser):
    profile_page_pers_info = ProfilePagePersInfo(browser)

    profile_page_pers_info.open2()

    profile_page_pers_info.p_open_prof_menu()
    profile_page_pers_info.p_open_profile()

    profile_page_pers_info.ed2_edit()
    profile_page_pers_info.ed2_name()
    profile_page_pers_info.ed2_pronouns()
    profile_page_pers_info.ed2_gender()
    profile_page_pers_info.ed2_choose_gender()

    profile_page_pers_info.ed2_save()
    browser.quit()
