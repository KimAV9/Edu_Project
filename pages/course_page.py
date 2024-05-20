from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from pages.registration_page import name
from pages.base_page import BasePage
import random
import allure
from time import sleep
import pytest

c_search_text_area = (By.XPATH, '//input[@class="react-autosuggest__input"]')
c_click_search = (By.XPATH, '//div[@class="browse-content-wrapper horizontal-box"]/descendant::div[@class="magnifier-wrapper"][2]')
c_click_course = (By.XPATH, '//div[@class="rc-MetatagsWrapper"]/descendant::a[@data-click-key="search.search.click.search_card"][1]')
c_click_continue = (By.XPATH, '//button[text()="Continue"]')

c_enroll = (By.XPATH, '//section/descendant::button[@data-e2e="enroll-button"]')
c_close_entry_window = (By.XPATH, '//div[@class="cds-Modal-container"]/descendant::button[1]')
c_close_goals_window = (By.XPATH, '//div[@data-track-app="learning_assistant"]/descendant::button[1]')

c_click_watch_intro = (By.XPATH, '//div[@class="rc-ModuleLessons"]/descendant::div[@role="presentation"][1]')
c_mark_complete = (By.XPATH, '//button[@data-testid="mark-complete"]')
c_read_project_overview = (By.XPATH, '//div[@class="item-tools-and-content-container"]/descendant::a[@data-testid="learner-app-client-navigation-link"][2]')
c_read_comm_disc = (By.XPATH, '//div[@class="item-tools-and-content-container"]/descendant::a[@data-testid="learner-app-client-navigation-link"][3]')
c_click_lab = (By.XPATH, '//div[@class="item-tools-and-content-container"]/descendant::a[@data-testid="learner-app-client-navigation-link"][4]')
c_click_quiz = (By.XPATH, '//div[@class="item-tools-and-content-container"]/descendant::a[@data-testid="learner-app-client-navigation-link"][5]')
c_click_survey = (By.XPATH, '//div[@class="item-tools-and-content-container"]/descendant::a[@data-testid="learner-app-client-navigation-link"][6]')


c_open_lab = (By.XPATH, '//main[@id="main"]//descendant::button[@data-track-app="open_course_home"]')
c_how_want_to_learn_open = (By.XPATH, '//div/descendant::button[@aria-describedby="byob-mode-description"][1]')
c_lab_instructions_close = (By.XPATH, '//section[@aria-label="Instructions"]/descendant::button[1]')


v_autoplay = (By.XPATH, '//button[@aria-label="Autoplay is on"]')
v_pause = (By.XPATH, '//button[@aria-label="Pause"]')
v_volume_slider = (By.XPATH, '//div[@class="rc-slider rc-VolumeSlider"]')
v_volume_mute = (By.XPATH, '//button[@aria-label="Mute"]')
v_save_note = (By.ID, 'save-note-button')
v_add_thoughts = (By.XPATH, '//div[@aria-labelledby="cds-react-aria-214-tab-NOTES"]/descendant::button[5]')
v_write_thoughts = (By.ID, 'note-text')
v_save_thoughts = (By.XPATH, '//button[@data-track-component= "edit_highlight"]')
v_view_all_notes = (By.XPATH, '//div[@aria-labelledby="cds-react-aria-214-tab-NOTES"]/descendant::a[@role= "button"]')
v_click_the_note = ()
v_check_timing = (By.XPATH, '//div[@aria-valuetext="* seconds"]')

t_start_assigment = (By.XPATH, '//button[@data-test="action-button"]')
t_answer1 = (By.XPATH, '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::span[@class="_1e7axzp"][1]')
t_answer2 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::span[@class="_1e7axzp"][4]')
t_answer3 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::span[@class="_1e7axzp"][7]')
t_answer4 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::span[@class="_1e7axzp"][10]')
t_answer5 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::span[@class="_1e7axzp"][13]')
t_answer6 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::span[@class="_1e7axzp"][19]')
t_answer7 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::span[@class="_1e7axzp"][21]')
t_answer8 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::span[@class="_1e7axzp"][25]')
t_answer9 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::span[@class="_1e7axzp"][28]')
t_answer10 = (By.XPATH,
              '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::span[@class="_1e7axzp"][31]')
t_answer11 = (By.XPATH,
              '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::span[@class="_1e7axzp"][37]')
t_answer12 = (By.XPATH,
              '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::span[@class="_1e7axzp"][38]')
t_agree_to_terms = (By.XPATH, '//input[@id="agreement-checkbox-base"]')
t_write_name = (By.XPATH, '//input[@class="css-opa93d"]')
t_submit = (By.XPATH, '//button[@data-test="submit-button"]')


class CoursePage(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def open(self):
        return self.browser.get('https://www.coursera.org/')

    @allure.step('Enter text')
    def search_course(self):
        return self.find(c_search_text_area).send_keys('Business Analysis & Process Management')

    @allure.step('Click search')
    def click_search(self):
        return self.find(c_click_search).click()

    @allure.step('Click Course')
    def click_course(self):
        return self.find(c_click_course).click()

    @allure.step('Enroll to course')
    def enroll(self):
        focus_window = self.browser.window_handles
        self.browser.switch_to.window(focus_window[0])
        self.browser.close()
        self.browser.switch_to.window(focus_window[-1])
        return self.find(c_enroll).click()

    @allure.step('Continue the course')
    def click_continue(self):
        return self.find(c_click_continue).click()

    @allure.step('Close commitment window')
    def close_commit_window(self):
        return self.find(c_close_entry_window).click()

    @allure.step('Close goals window')
    def close_goals_window(self):
        return self.find(c_close_goals_window).click()

    @allure.step('Watch introduction to course video')
    def watch_intro(self):
        return self.find(c_click_watch_intro).click()

    @allure.step('Click reading #1 page')
    def click_read1(self):
        return self.find(c_read_project_overview).click()

    @allure.step('Click "Mark as completed" reading #1')
    def click_complete(self):
        return self.find(c_mark_complete).click()

    @allure.step('Click reading #2 page')
    def click_read2(self):
        return self.find(c_read_comm_disc).click()

    @allure.step('Click "Mark as completed" reading #2')
    def click_complete2(self):
        return self.find(c_mark_complete).click()

    @allure.step('Click lab page')
    def click_lab(self):
        return self.find(c_click_lab).click()

    @allure.step('Click open lab')
    def click_open_lab(self):
        return self.find(c_open_lab).click()

    @allure.step('Click open lab task')
    def click_open_task(self):
        focus_window = self.browser.window_handles
        self.browser.switch_to.window(focus_window[1])
        self.find(c_how_want_to_learn_open).click()
        self.browser.switch_to.window(focus_window[-1])
        self.browser.close()
        self.browser.switch_to.window(focus_window[1])
        self.browser.close()
        sleep(10)
        self.browser.switch_to.window(focus_window[0])

    @allure.step('Click quiz page')
    def click_quiz(self):
        return self.find(c_click_quiz).click()

    @allure.step('Click start quiz')
    def click_start_quiz(self):
        return self.find(t_start_assigment).click()

    @allure.step('Answer questions')
    def answer_quiz(self):
        self.find(t_answer1).click()
        self.find(t_answer2).click()
        self.find(t_answer3).click()
        self.find(t_answer4).click()
        self.find(t_answer5).click()
        self.find(t_answer6).click()
        self.find(t_answer7).click()
        self.find(t_answer8).click()
        self.find(t_answer9).click()
        self.find(t_answer10).click()
        self.find(t_answer11).click()
        self.find(t_answer12).click()

    @allure.step('Accept the agreement')
    def click_i_understand(self):
        return self.find(t_agree_to_terms).click()

    @allure.step('Write name')
    def write_name(self):
        return self.find(t_write_name).send_keys(name)

    @allure.step('Submit quiz')
    def submit_quiz(self):
        return self.find(t_submit).click()

    @allure.step('Click survey')
    def click_survey(self):
        return self.find(c_click_survey).click()

    @allure.step('Click "Mark as completed" for quiz')
    def click_completed_survey(self):
        return self.find(c_mark_complete).click()

