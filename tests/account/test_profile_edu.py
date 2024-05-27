import allure
import pytest
from pages.profile_page import ProfilePageEducation
from time import sleep
import pytest_order


@allure.title('Test add education data in profile')
@allure.description('Изменение данных в профиле аккаунта об образовании')
@allure.tag('Account', 'Profile')
@allure.epic('Account')
@allure.feature('Profile')
@allure.story('Education')
@pytest.mark.order(12)
def test_education(browser):
    profile_page_edu = ProfilePageEducation(browser)

    profile_page_edu.open2()

    profile_page_edu.p_open_prof_menu()
    profile_page_edu.p_open_profile()

    profile_page_edu.e2_add_edu()
    profile_page_edu.e2_name_of_inst()
    profile_page_edu.e2_choose_inst()
    profile_page_edu.e2_degree()
    profile_page_edu.e2_choose_degree()

    profile_page_edu.e2_discipline()
    profile_page_edu.e2_choose_discipline()

    profile_page_edu.e2_area_of_conc()

    profile_page_edu.e2_start_month()
    profile_page_edu.e2_start_choose_month()
    profile_page_edu.e2_start_year()
    profile_page_edu.e2_start_choose_year()

    profile_page_edu.e2_end_month()
    profile_page_edu.e2_end_choose_month()
    profile_page_edu.e2_end_year()
    profile_page_edu.e2_end_choose_year()

    profile_page_edu.e2_cumulative_grade()
    profile_page_edu.e2_currently_study()

    profile_page_edu.e2_save()
    browser.quit()