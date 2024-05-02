import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from keyboard import press

browser = webdriver.Chrome
login = (By.XPATH, '//a[text() = "Log In"]')
login_email = (By.ID, 'email')
login_password = (By.ID, 'password')
login_button = (By.XPATH, '//button[@class = "_6dgzsvq css-j6v0dd"]')
search_button = (By.XPATH, '//input[@class="react-autosuggest__input"]')

c_subj = (By.XPATH, '//div[@data-testid="search-filter-group-Subject"]/descendant::span[@class="cds-199"][1]')
c_lang = (By.XPATH, '//div[@data-testid="search-filter-group-Language"]/descendant::span[@class= "cds-199"][1]')
c_prod = (By.XPATH, '//div[@data-testid="search-filter-group-Learning Product"]/descendant::span[@class= "cds-199"][1]')
c_lvl = (By.XPATH, '//div[@data-testid="search-filter-group-Level"]/descendant::span[@class= "cds-199"][1]')
c_dur = (By.XPATH, '//div[@data-testid="search-filter-group-Duration"]/descendant::span[@class= "cds-199"][1]')
c_skills = (By.XPATH, '//div[@data-testid="search-filter-group-Skills"]/descendant::span[@class= "cds-199"][1]')
c_subs = (By.XPATH, '//div[@data-testid="search-filter-group-Subtitles"]/descendant::span[@class= "cds-199"][1]')
c_edu = (By.XPATH, '//div[@data-testid="search-filter-group-Educator"]/descendant::span[@class= "cds-199"][1]')


class FilterCheck(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def open2(self):
        return self.main_page()

    @allure.step('Login into account')
    def login2(self):
        self.login()
        self.login_email()
        self.login_password()
        return self.login_button()

    @allure.step('Open search')
    def search(self):
        self.find(search_button).click()
        return press('enter')

    @allure.step('Choose subject')
    def subj_click(self):
        return self.find(c_subj).click()

    @allure.step('Choose language')
    def lang_click(self):
        return self.find(c_lang).click()

    @allure.step('Choose learning product')
    def prod_click(self):
        return self.find(c_prod).click()

    @allure.step('Choose level')
    def lvl_click(self):
        return self.find(c_lvl).click()

    @allure.step('Choose duration')
    def dur_click(self):
        return self.find(c_dur).click()

    @allure.step('Choose skills')
    def skills_click(self):
        return self.find(c_skills).click()

    @allure.step('Choose language of subtitles')
    def subs_click(self):
        return self.find(c_subs).click()

    @allure.step('Choose educator')
    def edu_click(self):
        return self.find(c_edu).click()

