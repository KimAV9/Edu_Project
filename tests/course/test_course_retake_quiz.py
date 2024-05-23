import allure
import pytest
from pages.course_page import RetakeTest
from time import sleep
import pytest_order

@pytest.mark.skip
@pytest.mark.order(19)
def test_retake_test(browser):
    retake_test = RetakeTest(browser)

    retake_test.temp_open()
    sleep(5)
    retake_test.open_quiz()
    retake_test.click_continue()
    retake_test.click_try_again()
    retake_test.check_if_capable()