import allure
import pytest
from pages.course_page import DeleteNotes
from time import sleep
import pytest_order

@allure.title('Test delete a note')
@allure.description('Создать заметку и удалить ее')
@allure.tag('Course', 'Video Player', 'Notes')
@allure.epic('Course')
@allure.feature('Notes')
@allure.story('Delete')
@allure.severity('Normal')
@pytest.mark.order(26)
def test_delete_notes(browser):
    delete_notes = DeleteNotes(browser)

    delete_notes.open()
    delete_notes.open_course()
    delete_notes.watch_intro()

    delete_notes.click_save_note()
    delete_notes.click_course_homepage()
    delete_notes.click_notes()

    delete_notes.click_delete()
    delete_notes.click_confirm_delete()
    browser.quit()
