import allure
from pages.general_page import DegreeFilterProgramLvl
import pytest
import pytest_order



@allure.title('Test degree filter')
@allure.description('Фильтрация успешна')
@allure.tag('Degree', 'Filter')
@allure.epic('General')
@allure.feature('Degrees')
@allure.story('Degree filter')
@allure.severity('Low')
@pytest.mark.order(6)
def test_degree_filter_program_lvl(browser):
    degree_filter_program_lvl = DegreeFilterProgramLvl(browser)

    degree_filter_program_lvl.open()
    degree_filter_program_lvl.click_program_lvl()
    degree_filter_program_lvl.choose_lvl()
    degree_filter_program_lvl.click_apply()

    degree_filter_program_lvl.assert_degree1()
    degree_filter_program_lvl.assert_degree2()

    degree_filter_program_lvl.check_degrees()
    browser.quit()