import allure
import pytest
from pages.course_page import AddThoughts
from time import sleep
import pytest_order

@pytest.mark.skip
@pytest.mark.order(16)
def test_add_thoughts(browser):
    add_thoughts = AddThoughts(browser)

    add_thoughts.temp_open()
    add_thoughts.click_save_note()
    add_thoughts.click_course_homepage()
    add_thoughts.click_notes()

    add_thoughts.click_edit_thoughts()
    add_thoughts.add_thoughts()
    add_thoughts.save_thoughts()
    add_thoughts.check_added_thoughts()

    browser.quit()