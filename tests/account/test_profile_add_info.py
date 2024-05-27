import allure
import pytest
from pages.profile_page import ProfilePageAddInfo
from time import sleep
import pytest_order


@allure.title('Test add additional data profile')
@allure.description('Произвести добавление данных в "Add additional info"')
@allure.tag('Account', 'Profile')
@allure.epic('Account')
@allure.feature('Profile')
@allure.story('Additional info')
@pytest.mark.order(11)
def test_additional_info(browser):
    profile_page_add_info = ProfilePageAddInfo(browser)

    profile_page_add_info.open2()

    profile_page_add_info.p_open_prof_menu()
    profile_page_add_info.p_open_profile()

    profile_page_add_info.i2_add_info()
    profile_page_add_info.i2_write_about()
    profile_page_add_info.i2_save()

    browser.quit()
