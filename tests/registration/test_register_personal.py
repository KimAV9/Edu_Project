import pytest
from pages.registration_page import Background
from time import sleep
import pytest_order

@pytest.mark.skip
def test_background(browser):
    background = Background(browser)

    background.open_page()

    background.write_work_occup()
    background.click_work_exp()
    background.choose_exp()
    background.write_employer()
    background.click_work_now()

    background.click_degree()
    background.choose_degree()
    background.click_field()
    background.choose_field()
    background.click_study_now()

    background.write_goal_occup()
    background.write_industry()

    background.click_cont()

    browser.quit()
