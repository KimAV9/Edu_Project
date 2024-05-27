import allure
import pytest
from pages.course_page import AddThoughts
from time import sleep
import pytest_order


@allure.title('Test add thoughts to the note')
@allure.description('Убедится что в заметку можно добавить свое описание')
@allure.tag('Course', 'Video Player', 'Notes')
@allure.epic('Course')
@allure.feature('Notes')
@allure.story('Add thoughts')
@pytest.mark.order(25)
def test_add_thoughts(browser):
    add_thoughts = AddThoughts(browser)

    add_thoughts.open()
    add_thoughts.open_course()

    add_thoughts.watch_intro()
    add_thoughts.click_save_note()

    add_thoughts.click_course_homepage()
    add_thoughts.click_notes()

    add_thoughts.click_edit_thoughts()
    add_thoughts.add_thoughts()
    add_thoughts.save_thoughts()
    add_thoughts.check_added_thoughts()

    browser.quit()
