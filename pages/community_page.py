from selenium.common import InvalidSelectorException
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from pages.registration_page import name
import random
import allure
from time import sleep
import pytest

import requests
from bs4 import BeautifulSoup

x = random.randint(1, 6)
y = random.randint(1, 3)

c_community = "https://www.coursera.support/s/community?language=en_US"
c_featured = (By.XPATH, f'//section[@role="tabpanel"]/descendant::a[@class="topicLink"][{random.randint(1, 6)}]')

c_click_tag = (By.XPATH,
               f'//div[@class="forceTopicSubTopicNavigation"]/descendant::a[@class="comm-topic__link"][{y}]')
c_tags_save = (By.XPATH,
               f'//div[@class="forceTopicSubTopicNavigation"]/descendant::span[@class="slds-col"][{y}]')

c_check_tags_after_search = (By.XPATH,
                             '//div[@data-feed-type]/descendant::div[@class="topic-topicContainer forceTopicSimpleTopicAssignments"][1]/descendant::span[@title]')

c_click_sort_by = (By.ID, 'combobox-button-514')
c_click_latest_post = (By.XPATH,
                       '//lightning-combobox[@class="feeds-sorter-trigger slds-form-element"]/descendant::*[@class="slds-media__body"][2]')


class TestTags(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_page(self):
        return self.browser.get(c_community)

    def click_featured(self):
        return self.find(c_featured).click()

    def click_tag(self):
        sleep(5)
        html_content = self.browser.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        find_tag = soup.find(c_tags_save)
        print(find_tag)
        tag = find_tag.text
        print(tag)
        self.find(c_click_tag).click()
        sleep(10)
