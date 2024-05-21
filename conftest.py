from selenium import webdriver
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser(headless_flg=False):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")
    options.add_argument(r"--user-data-dir=C:\Users\MSI\AppData\Local\Google\Chrome\User Data")
    options.add_argument("--profile-directory=Profile 1")
    if (headless_flg):
        options.add_argument('--headless')
    options.add_argument("start-maximized")
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(10)
    return chrome_browser
