import allure
import pytest
from pages.course_page import SavingNotesCheck
from time import sleep
import pytest_order


@pytest.mark.order(15)
def test_saving_notes_check(browser):
    saving_notes_check = SavingNotesCheck(browser)

    saving_notes_check.temp_open()
    saving_notes_check.click_save_note()
    saving_notes_check.check_video_notes_timing()
    saving_notes_check.save_video_notes_timing()
    saving_notes_check.click_course_homepage()

    saving_notes_check.click_notes()
    saving_notes_check.check_saved_notes_timing()
    saving_notes_check.save_notes_saved_timing()
    saving_notes_check.open_note()
    #saving_notes_check.click_notes_video()
    saving_notes_check.check_video_timing()
    saving_notes_check.save_video_timing()
    saving_notes_check.timing_check()
    browser.quit()
