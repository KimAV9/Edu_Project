from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
import random
import allure
from time import sleep
import pytest
import re

c_prof_menu = (By.XPATH, '//button[@data-track-component="profile_drop_down_btn"]')
c_updates = (By.XPATH, '//div[@class="header-right-nav-wrapper css-1h9ktwj"]/descendant::li[@role="menuitem"][14]')

upd_check = (By.XPATH, '//div[@data-e2e="simple-notification-subject" and text() = "Please confirm your email"]')

r_more_reviews = (By.XPATH, '//a[@data-track-component="reviews_module_view_more_cta"]')
r_review1 = (By.XPATH, '//div[@data-e2e="reviews-list"]/descendant::span[@class="cds-button-label"][1]')
r_review2 = (By.XPATH, '//div[@data-e2e="reviews-list"]/descendant::span[@class="cds-button-label"][2]')

l_click_language_menu = (By.XPATH, '//ul[@id = "authenticated-info-menu"]/descendant::li[@role="menuitem"][9]')
l_choose_language = (
By.XPATH, f'//div[@class="cds-popoverContainer-inner"]/descendant::div[text()!="English"][{random.randint(1, 16)}]')
l_choose_language_eng = (By.XPATH, '//div[@class="cds-popoverContainer-inner"]/descendant::div[text()="English"]')
l_check_translation = (By.XPATH, '//div[@data-testid="consumer-home-page"]/descendant::span[text()][1]')

x = random.randint(1, 2)

d_open_filter = (By.XPATH, '//div[@data-e2e="product-dropdown"]/child::button')
d_choose_lvl = (By.XPATH, f'//ul[@aria-label="Options list"]/child::li[{x}]')
d_apply = (By.XPATH, '//div[@class="cds-popoverContainer-inner"]/descendant::div/child::button[1]')
d_check1 = (By.XPATH, '//div[@data-test="TopProductsList"]/descendant::h3[@class="cds-CommonCard-title css-6ecy9b"][1]')
d_check2 = (By.XPATH, '//div[@data-test="TopProductsList"]/descendant::h3[@class="cds-CommonCard-title css-6ecy9b"][2]')


class CheckUpdates(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def open2(self):
        return self.main_page()

    @allure.step('Open account menu')
    def open_prof_menu(self):
        return self.find(c_prof_menu).click()

    @allure.step('Open updates page')
    def open_updates(self):
        return self.find(c_updates).click()

    @allure.step('Check the update')
    def check_updates(self):
        return self.find(upd_check)


class CheckReviewSort(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)
        more_reviews_link = None
        review1 = None
        review2 = None

    @allure.step('Open main page')
    def temp_open(self):
        return self.browser.get('https://www.coursera.org/learn/indigenous-canada')

    @allure.step('Find more reviews button')
    def more_reviews(self):
        return self.find(r_more_reviews)

    @allure.step('Open more reviews')
    def click_more_reviews2(self):
        more_reviews_link = self.more_reviews().get_attribute('href')
        self.browser.get(more_reviews_link)

    @allure.step('Find review number 1')
    def assert_review1(self):
        return self.find(r_review1)

    @allure.step('Find review number 2')
    def assert_review2(self):
        return self.find(r_review2)

    @allure.step('Compare if default review sorting by helpful is working as intended')
    def compare_reviews(self):
        review1 = self.assert_review1().text
        review2 = self.assert_review2().text
        numbers_review1 = int(re.search(r'\d+', review1).group())
        numbers_review2 = int(re.search(r'\d+', review2).group())
        if numbers_review1 > numbers_review2:
            return True
        else:
            print('Review error')


class DegreeFilterProgramLvl(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)
        degree1 = None
        degree2 = None

    @allure.step('Open main page')
    def temp_open(self):
        return self.browser.get('https://www.coursera.org/degrees')

    @allure.step('Open the filter for degree levels')
    def click_program_lvl(self):
        return self.find(d_open_filter).click()

    @allure.step('Choose a level of a degree')
    def choose_lvl(self):
        return self.find(d_choose_lvl).click()

    @allure.step('Apply settings to the filter')
    def click_apply(self):
        return self.find(d_apply).click()

    @allure.step('Check the first found degree')
    def assert_degree1(self):
        return self.find(d_check1)

    @allure.step('Check seconds found degree')
    def assert_degree2(self):
        return self.find(d_check2)

    @allure.step('Check if degrees found correspond to the filter settings')
    def check_degrees(self):
        degree1 = self.assert_degree1().text
        degree2 = self.assert_degree2().text

        if x == 1:
            if 'Bachelor' in degree1 and degree2:
                return True
        elif x == 2:
            if 'Master' in degree1 and degree2:
                return True


class CheckLocalization(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)
        translated_text = None

    @allure.step('Open main page')
    def open2(self):
        return self.main_page()

    @allure.step('Open language menu')
    def open_lang_menu(self):
        return self.find(l_click_language_menu).click()

    @allure.step('Choose a random language')
    def choose_lang(self):
        return self.find(l_choose_language).click()

    @allure.step('Choose english language')
    def choose_eng(self):
        return self.find(l_choose_language_eng).click()

    @allure.step('Find text to check for translation')
    def assert_text(self):
        return self.find(l_check_translation)

    @allure.step('Search text if it is in correct language')
    def check_lang(self):
        translated_text = self.assert_text().text
        result = bool(re.search('[a-zA-Z]', translated_text))
        return result

    @allure.step('Confirm the change')
    def confirm_localization(self):
        return self.check_lang()

    def confirm_lang_change1(self):
        if self.check_lang() is False:
            return True
