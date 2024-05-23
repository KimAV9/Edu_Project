import allure
from pages.settings_page import NotesAndHighlights
import pytest
import pytest_order


@allure.story('Change preferences on Notes&Highlights in settings')
@pytest.mark.order(10)
@pytest.mark.skip
def test_notes(browser):
    comm_pref = NotesAndHighlights(browser)

    comm_pref.open2()
    comm_pref.open_prof_menu()
    comm_pref.open_settings()
    comm_pref.open_notes()
    comm_pref.pres_switch()
    browser.quit()
