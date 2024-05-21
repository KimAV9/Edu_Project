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
b = [1]

c_community = "https://www.coursera.support/s/community?language=en_US"
c_featured = (By.XPATH, f'//section[@role="tabpanel"]/descendant::a[@class="topicLink"][{random.randint(1, 6)}]')

c_click_tag = (By.XPATH, f'//div[@class="forceTopicSubTopicNavigation"]/descendant::community_topic-topics-link[{y}]')
c_tags_save = (By.XPATH, f'//div[@class="forceTopicSubTopicNavigation"]/descendant::span[@class="slds-col"][{y}]')

c_check_tags_after_search = (By.XPATH, '//div[@data-feed-type]/descendant::a[1]/descendant::span[@title][1]')

c_click_sort_by = (By.ID, 'combobox-button-514')
c_click_latest_post = (By.XPATH,
                       '//lightning-combobox[@class="feeds-sorter-trigger slds-form-element"]/descendant::*[@class="slds-media__body"][2]')

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
ap_choice1 = (By.XPATH, '//div[@class="inputContainer"]/descendant::input[@data-interactive-lib-uid="3"]')
ap_choice2 = (By.XPATH, '//div[@class="inputContainer"]/descendant::input[@data-interactive-lib-uid="4"]')
ap_choice3 = (By.XPATH, '//div[@class="inputContainer"]/descendant::input[@data-interactive-lib-uid="5"]')
ap_ask = (
    By.XPATH, '//button[@class="slds-button slds-button_brand cuf-publisherShareButton qe-pollPostDesktop MEDIUM"]')


class TagsTesting(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.tag_click = None

    def open_page(self):
        return self.browser.get(c_community)

    def click_featured(self):
        return self.find(c_featured).click()

    def find_tag(self):
        return self.find(c_tags_save)

    def check_tag_to_click(self):
        self.tag_click = self.find_tag().text
        return self.tag_click

    def click_tag(self):
        return self.find(c_click_tag).click()

    def find_disc_tags(self):
        return self.find(c_check_tags_after_search)

    def check_tags(self):
        tag_check1 = self.find_disc_tags().text
        while True:
            try:
                if tag_check1 == self.tag_click:
                    return True
                break
            except Exception:
                b + 1
                self.find_disc_tags()


class AskQuestion(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_page(self):
        return self.browser.get(c_community)

    def click_featured(self):
        return self.find(c_featured).click()

    def click_question(self):
        return self.find(aq_click_question).click()

    def write_question(self):
        return self.find(aq_question_text_area).send_keys(text)

    def make_bold(self):
        return self.find(aq_click_bold).click()

    def make_italic(self):
        return self.find(aq_click_italic).click()

    def make_strikethrough(self):
        return self.find(aq_click_strikethrough).click()

    def make_underline(self):
        return self.find(aq_click_underline).click()

    def make_bulletin_list(self):
        return self.find(aq_click_bulleted_list).click()

    def write_details(self):
        return self.find(aq_details_text_area).send_keys('asd')

    def click_emoji_menu(self):
        return self.find(aq_click_emoji).click()

    def choose_emoji(self):
        return self.find(aq_choose_emoji).click()

    def check_text(self):
        return self.find(aq_check_text).click()
