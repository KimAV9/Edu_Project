import allure
from pages.general_page import CheckUpdates
import pytest
import pytest_order


@pytest.mark.order(26)
@pytest.mark.skip
def test_check_updts(browser):
    check_updts = CheckUpdates(browser)

    check_updts.open2()
    check_updts.open_prof_menu()
    check_updts.open_updates()

    check_updts.check_updates()
    browser.quit()