import allure
import pytest
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from keyboard import press
from time import sleep
import random
from pages.registration_page import RandomGenerator

browser = webdriver.Chrome
login = (By.XPATH, '//a[text() = "Log In"]')
login_email = (By.ID, 'email')
login_password = (By.ID, 'password')
login_button = (By.XPATH, '//button[@class = "_6dgzsvq css-j6v0dd"]')
search_button = (By.XPATH, '//input[@class="react-autosuggest__input"]')

c_prof_menu = (By.XPATH, '//button[@data-track-component="profile_drop_down_btn"]')
c_settings = (By.XPATH, '//div[@class="header-right-nav-wrapper css-1h9ktwj"]/descendant::li[@role="menuitem"][13]')

c_fullname_field = (By.ID, 'settings-basic-full-name')
c_email_field = (By.ID, 'settings-basic-email')
c_timezone_menu = (By.ID, 'settings-basic-timezone')
c_timezone_select = (By.XPATH, f'//select[@name="timezone"]/descendant::option[{random.randint(1, 417)}]')
c_language_menu = (By.ID, 'settings-basic-language')
c_lang_select = (By.XPATH, '//select[@name="locale"]/descendant::option[1]')
c_save_button = (By.XPATH, '//div[@class="rc-BasicInformation"]//child::span[@class="cds-button-label"]')

text = RandomGenerator().generate_text()
email = RandomGenerator().generate_email()

p_current_password = (By.ID, 'settings-password-current')
p_new_password = (By.ID, 'settings-password-new')
p_retype_password = (By.ID, 'settings-password-new-confirm')
p_change_password = (By.XPATH, '//div[@class="rc-Password"]/descendant::button')
p_confirm_password = (By.XPATH, '//span[@class="rc-StatusMessage success"]')

com_open = (By.XPATH, '//*[@id="rendered-content"]/descendant::div[@class="cds-MenuListItem-content"][2]')
com_opt_out = (By.XPATH, '//div[@class="rc-EmailPreferences"]/descendant::input[1]')
com_pers_recom = (By.XPATH, '//div[@class="rc-EmailPreferences"]/descendant::input[2]')
com_notif_promo = (By.XPATH, '//div[@class="rc-EmailPreferences"]/descendant::input[3]')
com_info_degr = (By.XPATH, '//div[@class="rc-EmailPreferences"]/descendant::input[4]')
com_surv = (By.XPATH, '//div[@class="rc-EmailPreferences"]/descendant::input[5]')
com_save = (By.XPATH, '//div[@class="rc-EmailPreferences"]/descendant::button[1]')

com_proj_netw = (By.ID, '565')
com_save2 = (By.XPATH, '//div[@class="rc-EmailPreferences"]/descendant::button[3]')


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
        self.find(c_fullname_field).clear()
        return self.find(c_fullname_field).send_keys(text)

    @allure.step('Write new email')
    def write_email_field(self):
        self.find(c_email_field).clear()
        return self.find(c_email_field).send_keys('Tobey123@Mark.com')

    @allure.step('Open timezone dropdown menu')
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


class PasswordChange(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def open2(self):
        return self.main_page()

    @allure.step('Open account menu')
    def open_prof_menu(self):
        return self.find(c_prof_menu).click()

    @allure.step('Open settings page')
    def open_settings(self):
        return self.find(c_settings).click()

    @allure.step('Enter current password')
    def write_current_password(self):
        return self.find(p_current_password).send_keys("KappaKeepo1423")

    @allure.step('Enter new password')
    def write_new_password(self):
        return self.find(p_new_password).send_keys('KappaKeepoq1w2e3')

    @allure.step('Retype new password')
    def retype_new_password(self):
        return self.find(p_retype_password).send_keys('KappaKeepoq1w2e3')

    @allure.step('Change password')
    def click_change_password(self):
        return self.find(p_change_password).click()

    @allure.step('Check for update')
    def check_password(self):
        return self.find(p_confirm_password)


class CommunicationPreferences(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def open2(self):
        return self.main_page()

    @allure.step('Open account menu')
    def open_prof_menu(self):
        return self.find(c_prof_menu).click()

    @allure.step('Open settings page')
    def open_settings(self):
        return self.find(c_settings).click()

    @allure.step('Open Communication Preferences')
    def open_comm_pref(self):
        return self.find(com_open).click()

    @allure.step('Click Opt-out of all Coursera emails (Optional)')
    def click_opt_out(self):
        return self.find(com_opt_out).click()

    @allure.step('Click Weekly personalized course recommendations')
    def click_pers_recom(self):
        while True:
            try:
                self.find(com_pers_recom).click()
                break
            except ElementClickInterceptedException:
                self.find(com_opt_out).click()


    @allure.step('Click Weekly notifications about promotions, new courses and programs, and special events')
    def click_notif_promo(self):
        return self.find(com_notif_promo)

    @allure.step('Click Information on online Master’s and Bachelor’s Degree programs')
    def click_info_degr(self):
        return self.find(com_info_degr).click()

    @allure.step('Click Surveys and invitations to help us improve Coursera content and your experience')
    def click_surv(self):
        return self.find(com_surv).click()

    @allure.step('Save changes')
    def save1(self):
        return self.find(com_save).click()

    @allure.step('Click Coursera Project Network')
    def click_proj_netw(self):
        return self.find(com_proj_netw).click()

    @allure.step('Save changes')
    def save2(self):
        return self.find(com_save2).click()
