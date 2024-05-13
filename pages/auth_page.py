from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.registration_page import password
import random
import allure
from time import sleep


login = (By.XPATH, '//a[text() = "Log In"]')
login_email = (By.ID, 'email')
login_password = (By.ID, 'password')
login_button = (By.XPATH, '//button[@class = "_6dgzsvq css-j6v0dd"]')
captcha = (By.XPATH, '//*[@id="rc-imageselect"]/div[3]/div[2]/div[1]/div[2]')
captcha2 = (By.XPATH, '//iframe[@title="recaptcha challenge expires in two minutes"]')
captcha3 = (By.XPATH, '//button[@class="rc-button-default goog-inline-block"]')
audio = (By.XPATH, '//*[@id="recaptcha-audio-button"]')


class AuthPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def open(self):
        return self.main_page()

    @allure.step('Click to open login page')
    def login(self):
        return self.find(login).click()

    @allure.step('Enter Email')
    def login_email(self):
        self.find(login_email).click()
        return self.find(login_email).send_keys('tobex26655@evimzo.com')

    @allure.step('Enter Password')
    def login_password(self):
        self.find(login_password).click()
        return self.find(login_password).send_keys('KappaKeepo1423')

    @allure.step('Click login button')
    def login_button(self):
        self.find(login_button).click()
        sleep(5)
