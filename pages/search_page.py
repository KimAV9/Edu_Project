import random

import pytest
import allure
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from time import sleep

browser = webdriver.Chrome
login = (By.XPATH, '//a[text() = "Log In"]')
login_email = (By.ID, 'email')
login_password = (By.ID, 'password')
login_button = (By.XPATH, '//button[@class = "_6dgzsvq css-j6v0dd"]')
search_button = (By.XPATH, '//form[@class="search-form"]/descendant::div[@class="magnifier-wrapper"][2]')
c_text_area = (By.XPATH, '//input[@class="react-autosuggest__input"]')

c_apply = (By.XPATH, '//div[@data-testid="scroll-container"]/descendant::button[2]')
c_choose_rand = (
    By.XPATH, f'//div[@aria-labelledby="checkbox-group"]/descendant::span[@class="cds-199"][{random.randint(1, 3)}]')
c_choose = (By.XPATH, '//div[@aria-labelledby="checkbox-group"]/descendant::span[@class="cds-199"][1]')

c_find_more_subj = (By.XPATH, '//div[1]/descendant::button[@data-test="expand-filter-items-button"][1]')
c_subj = (By.XPATH, '//div[@data-testid="search-filter-group-Subject"]/descendant::span[@class="cds-199"][1]')

c_lang = (By.XPATH, '//div[@data-testid="search-filter-group-Language"]/descendant::span[@class= "cds-199"][1]')
c_find_more_lang = (By.XPATH, '//div[1]/descendant::button[@data-test="expand-filter-items-button"][2]')

c_prod = (By.XPATH, '//div[@data-testid="search-filter-group-Learning Product"]/descendant::span[@class= "cds-199"][1]')
c_prod_rand = (
    By.XPATH, f'//div[@data-testid="search-filter-group-Learning Product"]/descendant::span[@class= "cds-199"][{random.randint(1, 3)}]')

c_lvl = (By.XPATH, '//div[@data-testid="search-filter-group-Level"]/descendant::span[@class= "cds-199"][1]')
c_lvl_rand = (By.XPATH, f'//div[@data-testid="search-filter-group-Level"]/descendant::span[@class= "cds-199"][{random.randint(1, 4)}]')

c_dur = (By.XPATH, '//div[@data-testid="search-filter-group-Duration"]/descendant::span[@class= "cds-199"][1]')
c_dur_rand = (By.XPATH, f'//div[@data-testid="search-filter-group-Duration"]/descendant::span[@class= "cds-199"][{random.randint(1, 6)}]')

c_skills = (By.XPATH, '//div[@data-testid="search-filter-group-Skills"]/descendant::span[@class= "cds-199"][1]')
c_find_more_skills = (By.XPATH, '//div[1]/descendant::button[@data-test="expand-filter-items-button"][3]')

c_subs = (By.XPATH, '//div[@data-testid="search-filter-group-Subtitles"]/descendant::span[@class= "cds-199"][1]')
c_find_more_subs = (By.XPATH, '//div[1]/descendant::button[@data-test="expand-filter-items-button"][4]')

c_edu = (By.XPATH, '//div[@data-testid="search-filter-group-Educator"]/descendant::span[@class= "cds-199"][1]')
c_find_more_edu = (By.XPATH, '//div[1]/descendant::button[@data-test="expand-filter-items-button"][5]')


class FilterCheck(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def open2(self):
        return self.main_page()

    @allure.step('Type text')
    def type_text(self):
        return self.find(c_text_area).send_keys('a')

    @allure.step('Open search')
    def search(self):
        return self.find(search_button).click()

    @allure.step('Choose subject')
    def subj_click(self):
        sleep(1)
        try:
            try:
                self.find(c_find_more_subj).click()
                self.find(c_choose_rand).click()
                return self.find(c_apply).click()
            except NoSuchElementException:
                self.find(c_choose).click()
                return self.find(c_apply).click()
        except NoSuchElementException:
            return self.find(c_subj).click()

    @allure.step('Choose language')
    def lang_click(self):
        sleep(1)
        try:
            try:
                self.find(c_find_more_lang).click()
                self.find(c_choose_rand).click()
                return self.find(c_apply).click()
            except NoSuchElementException:
                self.find(c_choose).click()
                return self.find(c_apply).click()
        except NoSuchElementException:
            return self.find(c_lang).click()

    @allure.step('Choose learning product')
    def prod_click(self):
        try:
            return self.find(c_prod_rand).click()
        except NoSuchElementException:
            return self.find(c_prod).click()

    @allure.step('Choose level')
    def lvl_click(self):
        try:
            return self.find(c_lvl_rand).click()
        except NoSuchElementException:
            return self.find(c_lvl).click()

    @allure.step('Choose duration')
    def dur_click(self):
        try:
            return self.find(c_dur_rand).click()
        except NoSuchElementException:
            return self.find(c_dur).click()

    @allure.step('Choose skills')
    def skills_click(self):
        sleep(1)
        try:
            try:
                self.find(c_find_more_skills).click()
                self.find(c_choose_rand).click()
                return self.find(c_apply).click()
            except NoSuchElementException:
                self.find(c_choose).click()
                return self.find(c_apply).click()
        except NoSuchElementException:
            return self.find(c_skills).click()

    @allure.step('Choose language of subtitles')
    def subs_click(self):
        sleep(1)
        try:
            try:
                self.find(c_find_more_lang).click()
                self.find(c_choose_rand).click()
                return self.find(c_apply).click()
            except NoSuchElementException:
                self.find(c_choose).click()
                return self.find(c_apply).click()
        except NoSuchElementException:
            return self.find(c_lang).click()

    @allure.step('Choose educator')
    def edu_click(self):
        sleep(1)
        try:
            try:
                self.find(c_find_more_edu).click()
                self.find(c_choose_rand).click()
                return self.find(c_apply).click()
            except NoSuchElementException:
                self.find(c_choose).click()
                return self.find(c_apply).click()
        except NoSuchElementException:
            return self.find(c_edu).click()
