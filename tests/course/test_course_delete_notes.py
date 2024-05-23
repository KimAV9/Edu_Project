import allure
import pytest
from pages.course_page import DeleteNotes
from time import sleep
import pytest_order

@pytest.mark.skip
def test_delete_notes(browser):
    delete_notes = DeleteNotes(browser)

    delete_notes.temp_open()
    delete_notes.click_save_note()
    delete_notes.click_course_homepage()
    delete_notes.click_notes()

    delete_notes.click_delete()
    delete_notes.click_confirm_delete()
    browser.quit()
