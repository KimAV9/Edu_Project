import allure
from pages.general_page import CheckUpdates
import pytest
import pytest_order


@allure.title('Test updates')
@allure.description('При выполнение определенных действий получить обновлений об аккаунте')
@allure.tag('Updates')
@allure.epic('Updates')
@allure.story('Update check')
@allure.severity('Normal')
@pytest.mark.order(4)
def test_check_updts(browser):
    check_updts = CheckUpdates(browser)

    check_updts.open2()
    check_updts.open_prof_menu()
    check_updts.open_updates()

    check_updts.check_updates()
    browser.quit()