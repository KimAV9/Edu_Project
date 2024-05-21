from selenium import webdriver
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument(r"--user-data-dir=C:\Users\MSI\AppData\Local\Google\Chrome\User Data")
    options.add_argument("--profile-directory=Profile 1")
    options.add_argument("start-maximized")
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(10)
    return chrome_browser
