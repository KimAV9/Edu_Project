import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from keyboard import press
from time import sleep
import random

browser = webdriver.Chrome
login = (By.XPATH, '//a[text() = "Log In"]')
login_email = (By.ID, 'email')
login_password = (By.ID, 'password')
login_button = (By.XPATH, '//button[@class = "_6dgzsvq css-j6v0dd"]')
search_button = (By.XPATH, '//input[@class="react-autosuggest__input"]')

c_prof_menu = (By.XPATH, '//button[@data-track-component="profile_drop_down_btn"]')
c_settings = (By.XPATH,
              '//li[@class="rc-AuthenticatedAccountDropdown c-ph-right-nav-button c-ph-right-nav-desktop-only c-ph-avatar-button c-ph-right-nav-no-border c-ph-right-nav-expanded css-j4mi9a"]/descendant::a[@data-track-href="/account-settings"][1]')

c_fullname_field = (By.ID, 'settings-basic-full-name')
c_email_field = (By.ID, 'settings-basic-email')
c_timezone_menu = (By.ID, 'settings-basic-timezone')
c_timezone_select = (By.XPATH, f'//select[@name="timezone"]/descendant::option[{random.randint(1, 417)}]')
c_language_menu = (By.ID, 'settings-basic-language')
c_lang_select = (By.XPATH, '//select[@name="locale"]/descendant::option[1]')
c_save_button = (By.XPATH, '//div[@class="rc-BasicInformation"]//child::span[@class="cds-button-label"]')


class RandomGenerator:
    def __init__(self, min_length=4, max_length=10):
        self.vowels = "aeiou"
        self.consonants = "bcdghjklmnpqrstvwxyz"
        self.numbers = "0123456789"
        self.min_length = min_length
        self.max_length = max_length

    def generate_name(self):
        length = random.randint(self.min_length, self.max_length)
        gen_name = "".join(random.choice(self.consonants + self.vowels) for x in range(length))
        return gen_name.capitalize()

    def generate_password(self):
        length = random.randint(8, 12)
        gen_password = "".join(random.choice(self.consonants + self.vowels + self.numbers) for x in range(length))
        print(gen_password)
        return gen_password

    def generate_email(self):
        return self.generate_name() + ('@cats.meows')


text = RandomGenerator().generate_name()
email = RandomGenerator().generate_email()


class AccountSettings(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def open2(self):
        return self.main_page()

    @allure.step('Login')
    def login2(self):
        self.login()
        self.login_email()
        self.login_password()
        return self.login_button()

    @allure.step('Open account menu')
    def open_prof_menu(self):
        return self.find(c_prof_menu).click()

    @allure.step('Open settings page')
    def open_settings(self):
        return self.find(c_settings).click()

    @allure.step('Write new name')
    def write_fullname_field(self):
        return self.find(c_fullname_field).sendkeys(text)

    @allure.step('Write new email')
    def write_email_field(self):
        return self.find(c_email_field).send_keys(email)

    @allure.step('Open timizone dropdown menu')
    def click_timezone_menu(self):
        return self.find(c_timezone_menu).click()

    @allure.step('Select timezone')
    def click_timezone_select(self):
        return self.find(c_timezone_select).click()

    @allure.step('Open language dropdown menu')
    def click_language_menu(self):
        return self.find(c_language_menu).click()

    @allure.step('Choose language')
    def click_lang_select(self):
        return self.find(c_lang_select).click()

    @allure.step('Save changes')
    def click_save_button(self):
        return self.find(c_save_button).click()
