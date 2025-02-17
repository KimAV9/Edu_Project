from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from pages.base_page import BasePage
import random
import allure
from time import sleep
import pytest
from bs4 import BeautifulSoup

x = random.randint(1, 6)
y = random.randint(1, 3)
text = ("234")

c_community = "https://www.coursera.support/s/community?language=en_US"
c_featured = (By.XPATH, f'//section[@role="tabpanel"]/descendant::a[@class="topicLink"][{random.randint(1, 3)}]')

c_click_tag = (By.XPATH, f'//div[@class="forceTopicSubTopicNavigation"]/descendant::community_topic-topics-link[{y}]')
c_tags_save = (By.XPATH, f'//div[@class="forceTopicSubTopicNavigation"]/descendant::span[@class="slds-col"][{y}]')



c_click_sort_by = (By.ID, 'combobox-button-514')
c_click_latest_post = (By.XPATH,
                       '//lightning-combobox[@class="feeds-sorter-trigger slds-form-element"]/descendant::*[@class="slds-media__body"][2]')

aq_login = (By.XPATH, '//button[@title="Log in"]')
aq_accept = (By.XPATH, '//input[@value="Accept"]')
aq_click_question = (By.XPATH, '//a[@data-tab-name="FeedItem.QuestionPost"]/descendant::span[@class="title"]')
aq_question_text_area = (By.XPATH, '//div[@class="questiontitle input-field"]/descendant::textarea')
aq_details_text_area = (By.XPATH, '//div[@id="outerContainer"]/descendant::div[@role="textbox"]')
aq_click_bold = (By.XPATH, '//div[@class="questionbody input-field"]/descendant::button[@title="Bold"]')
aq_click_italic = (By.XPATH, '//div[@class="questionbody input-field"]/descendant::button[@title="Italic"]')
aq_click_underline = (By.XPATH, '//div[@class="questionbody input-field"]/descendant::button[@title="Underline"]')
aq_click_strikethrough = (
    By.XPATH, '//div[@class="questionbody input-field"]/descendant::button[@title="Strikethrough"]')
aq_click_bulleted_list = (
    By.XPATH, '//div[@class="questionbody input-field"]/descendant::button[@title="Bulleted List"]')
aq_click_emoji = (By.XPATH, '//div[@class="questionbody input-field"]/descendant::button[@title="Insert Emoji"]')
aq_choose_emoji = (By.XPATH, '//section[@data-name="Smileys & People"]/descendant::span[@class="emoji-entity"][1]')
aq_check_text = (By.XPATH, '//ul/li/strong/em/strike/u[text()="asd"]')
aq_ask_question = (By.XPATH,
                   '//button[@class="slds-button slds-button_brand cuf-publisherShareButton qe-questionPostDesktop MEDIUM"]')

ap_click_poll = (By.XPATH, '//div[@role="tablist"]/descendant::span[@class="title"][3]')
ap_write_question = (By.XPATH, '//div[@id="outerContainer"]/descendant::textarea')
ap_add_choice = (By.XPATH, '//button[@class="slds-button slds-button_brand cuf-addChoiceButton"]')
ap_choice1 = (By.XPATH, '(//div[@class="inputContainer"])[1]/descendant::input')
ap_choice2 = (By.XPATH, '(//div[@class="inputContainer"])[2]/descendant::input')
ap_choice3 = (By.XPATH, '(//div[@class="inputContainer"])[3]/descendant::input')
ap_ask = (
    By.XPATH, '//button[@class="slds-button slds-button_brand cuf-publisherShareButton qe-pollPostDesktop MEDIUM"]')


class TagsTesting(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.b = 1
        self.tag_click = None

    @allure.step('Open community page')
    def open_page(self):
        return self.browser.get(c_community)

    @allure.step('Open Featured')
    def click_featured(self):
        return self.find(c_featured).click()

    @allure.step('Find and save tag')
    def find_tag(self):
        sleep(3)
        return self.find(c_tags_save)

    @allure.step('Click on one of tags')
    def check_tag_to_click(self):
        self.tag_click = self.find_tag().text
        return self.tag_click

    @allure.step('Click on saved tag')
    def click_tag(self):
        return self.find(c_click_tag).click()

    @allure.step('Find tag in discussion')
    def find_disc_tags(self):
        sleep(3)
        while True:
            try:
                c_check_tags_after_search = (By.XPATH, f'//div[@data-feed-type]/descendant::a[{self.b}]/descendant::span[@title][1]')
                self.find(c_check_tags_after_search)
                break
            except NoSuchElementException:
                self.browser.navigate().back()
                self.find_tag()
                self.check_tags()
                self.click_tag()
            finally:
                c_check_tags_after_search = (
                    By.XPATH, f'//div[@data-feed-type]/descendant::a[{self.b}]/descendant::span[@title][1]')
                return self.find(c_check_tags_after_search)


    @allure.step('Check if found tags match')
    def check_tags(self):
        tag_check1 = self.find_disc_tags().text
        while True:
            try:
                self.b += 1
                if tag_check1 == self.tag_click:
                    break
            except tag_check1 != self.tag_click:
                self.find_disc_tags()


class AskQuestion(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open community page')
    def open_page(self):
        return self.browser.get(c_community)

    @allure.step('Open Featured')
    def click_featured(self):
        return self.find(c_featured).click()

    @allure.step('Log in')
    def log_in(self):
        try:
            self.find(aq_login).click()
            self.find(aq_accept).click()
        except NoSuchElementException:
            return True

    @allure.step('Click on write question')
    def click_question(self):
        sleep(5)
        return self.find(aq_click_question).click()

    @allure.step('Write question')
    def write_question(self):
        return self.find(aq_question_text_area).send_keys(text)

    @allure.step('Turn on bold text')
    def make_bold(self):
        return self.find(aq_click_bold).click()

    @allure.step('Turn on italics text')
    def make_italic(self):
        return self.find(aq_click_italic).click()

    @allure.step('Turn on strikethrough text')
    def make_strikethrough(self):
        return self.find(aq_click_strikethrough).click()

    @allure.step('Turn on underline text')
    def make_underline(self):
        return self.find(aq_click_underline).click()

    @allure.step('Turn on bulletin list')
    def make_bulletin_list(self):
        return self.find(aq_click_bulleted_list).click()

    @allure.step('Write details')
    def write_details(self):
        return self.find(aq_details_text_area).send_keys('asd')

    @allure.step('Check if text is corresponding to conditions')
    def check_text(self):
        return self.find(aq_check_text).click()

class AskPoll(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open community page')
    def open_page(self):
        return self.browser.get(c_community)

    @allure.step('Open Featured')
    def click_featured(self):
        return self.find(c_featured).click()

    @allure.step('Log in')
    def log_in(self):
        try:
            self.find(aq_login).click()
            self.find(aq_accept).click()
        except NoSuchElementException:
            return True
    @allure.step('Open poll')
    def click_poll(self):
        return self.find(ap_click_poll).click()

    @allure.step('Add another option')
    def add_option(self):
        return self.find(ap_add_choice).click()

    @allure.step('Write question')
    def write_question(self):
        return self.find(ap_write_question).send_keys(text)

    @allure.step('Write options')
    def write_options(self):
        self.find(ap_choice1).send_keys(text)
        self.find(ap_choice2).send_keys(text)
        self.find(ap_choice3).send_keys(text)

    @allure.step('Conduct poll')
    def click_ask(self):
        return self.find(ap_ask).click()
