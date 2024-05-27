import allure
from pages.settings_page import NotesAndHighlights
import pytest
import pytest_order


@allure.title('Test change Notes & Highlights preferences in profile')
@allure.description('Изменить предпочтения в во вкладке "Notes & Highlights" в настройках')
@allure.tag('Account', 'Settings')
@allure.epic('Account')
@allure.feature('Settings')
@allure.story('Notes&Highlights')
@pytest.mark.order(20)
def test_notes(browser):
    comm_pref = NotesAndHighlights(browser)

    comm_pref.open2()
    comm_pref.open_prof_menu()
    comm_pref.open_settings()
    comm_pref.open_notes()
    comm_pref.pres_switch()
    browser.quit()
