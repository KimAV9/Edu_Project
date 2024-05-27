import pytest
from pages.registration_page import Background
from time import sleep
import pytest_order
import allure


@allure.title('Test personal data for personalization')
@allure.description('Успешное заполнение данных для персонализации и сохранение их профиле')
@allure.tag('Registration', 'Personalization')
@allure.epic('Registration')
@allure.feature('Personalization')
@allure.story('Add personalization data to the account')
@allure.severity('Normal')
@pytest.mark.order(2)
def test_background(browser):
    background = Background(browser)

    background.open_page()

    background.write_work_occup()
    background.click_work_exp()
    background.choose_exp()
    background.write_employer()
    background.click_work_now()

    background.click_degree()
    background.choose_degree()
    background.click_field()
    background.choose_field()
    background.click_study_now()

    background.write_goal_occup()
    background.write_industry()

    background.click_cont()

    background.open_prof_menu()
    background.open_profile()

    background.click_edit_wk_pref()
    background.remove_wk_pref()
    background.save_wk_pref()

    browser.quit()
