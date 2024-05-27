import allure
import pytest
from pages.course_page import SavingNotesCheck
from time import sleep
import pytest_order

@allure.title('Test create a note')
@allure.description('Создать заметку и убедится что она работает')
@allure.tag('Course', 'Video Player', 'Notes')
@allure.epic('Course')
@allure.feature('Notes')
@allure.story('Save')
@allure.severity('Normal')
@pytest.mark.order(24)
def test_saving_notes_check(browser):
    saving_notes_check = SavingNotesCheck(browser)

    saving_notes_check.open()
    saving_notes_check.open_course()

    saving_notes_check.watch_intro()
    saving_notes_check.click_save_note()
    saving_notes_check.click_course_homepage()

    saving_notes_check.click_notes()
    saving_notes_check.saved_note_check()

    browser.quit()
