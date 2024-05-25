from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from pages.registration_page import name
from pages.base_page import BasePage
import random
import allure
from time import sleep
from selenium.webdriver import ActionChains, Keys
import pytest

e_search_text_area = (By.XPATH, '//input[@class="react-autosuggest__input"]')
e_click_search = (
    By.XPATH, '//div[@class="browse-content-wrapper horizontal-box"]/descendant::div[@class="magnifier-wrapper"][2]')
e_click_course = (
    By.XPATH, '//div[@class="rc-MetatagsWrapper"]/descendant::a[@data-click-key="search.search.click.search_card"][1]')
e_click_continue = (By.XPATH, '//button[text()="Continue"]')

e_enroll = (By.XPATH, '//section/descendant::button[@data-e2e="enroll-button"]')
e_close_entry_window = (By.XPATH, '//div[@class="cds-Modal-container"]/descendant::button[1]')
e_close_goals_window = (By.XPATH, '//div[@data-track-app="learning_assistant"]/descendant::button[1]')

c_open_course = (By.XPATH, '//div[@class="rc-LoggedInHome-CourseCards css-53xei8"]/descendant::a[1]')
c_click_watch_intro = (By.XPATH, '//div[@class="rc-ModuleLessons"]/descendant::div[@role="presentation"][1]')
c_mark_complete = (By.XPATH, '//button[@data-testid="mark-complete"]')
c_read_project_overview = (By.XPATH,
                           '//div[@class="item-tools-and-content-container"]/descendant::a[@data-testid="learner-app-client-navigation-link"][2]')
c_read_comm_disc = (By.XPATH,
                    '//div[@class="item-tools-and-content-container"]/descendant::a[@data-testid="learner-app-client-navigation-link"][3]')
c_click_lab = (By.XPATH,
               '//div[@class="item-tools-and-content-container"]/descendant::a[@data-testid="learner-app-client-navigation-link"][4]')
c_click_quiz = (By.XPATH,
                '//div[@class="item-tools-and-content-container"]/descendant::a[@data-testid="learner-app-client-navigation-link"][5]')
c_click_survey = (By.XPATH,
                  '//div[@class="item-tools-and-content-container"]/descendant::a[@data-testid="learner-app-client-navigation-link"][6]')

c_open_lab = (By.XPATH, '//main[@id="main"]//descendant::button[@data-track-app="open_course_home"]')
c_how_want_to_learn_open = (By.XPATH, '//div/descendant::button[@aria-describedby="byob-mode-description"][1]')
c_lab_instructions_close = (By.XPATH, '//section[@aria-label="Instructions"]/descendant::button[1]')

v_autoplay = (By.XPATH, '//button[@aria-label="Autoplay is on"]')
v_pause = (By.XPATH, '//button[@aria-label="Pause"]')
v_volume_slider = (By.XPATH, '//div[@class="rc-slider rc-VolumeSlider"]')
v_volume_mute = (By.XPATH, '//button[@aria-label="Mute"]')
v_save_note = (By.ID, 'save-note-button')
v_click_notes_in_video = (By.XPATH, '//button[@data-track-component="focused_lex_lecture_tabs_notes"]')
v_add_thoughts = (By.XPATH, '//div[@aria-labelledby="cds-react-aria-214-tab-NOTES"]/descendant::button[5]')
v_write_thoughts = (By.ID, 'note-text')
v_save_thoughts = (By.XPATH, '//button[@data-track-component= "edit_highlight"]')
v_view_all_notes = (By.XPATH, '//div[@aria-labelledby="cds-react-aria-214-tab-NOTES"]/descendant::a[@role= "button"]')
v_click_the_note = ()
v_check_timing = (By.XPATH, '//div[@aria-valuetext="* seconds"]')

t_start_assigment = (By.XPATH, '//button[@data-tests="action-button"]')
t_cont = (By.XPATH, '//button[@data-tests="continue-button"]')
t_answer1 = (By.XPATH, '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::div[@class="rc-Option"][1]')
t_answer2 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::div[@class="rc-Option"][4]')
t_answer3 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::div[@class="rc-Option"][7]')
t_answer4 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::div[@class="rc-Option"][10]')
t_answer5 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::div[@class="rc-Option"][13]')
t_answer6 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::div[@class="rc-Option"][19]')
t_answer7 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::div[@class="rc-Option"][21]')
t_answer8 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::div[@class="rc-Option"][25]')
t_answer9 = (By.XPATH,
             '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::div[@class="rc-Option"][28]')
t_answer10 = (By.XPATH,
              '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::div[@class="rc-Option"][31]')
t_answer11 = (By.XPATH,
              '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::div[@class="rc-Option"][37]')
t_answer12 = (By.XPATH,
              '//div[@id="TUNNELVISIONWRAPPER_CONTENT_ID"]/descendant::div[@class="rc-Option"][38]')
t_agree_to_terms = (By.XPATH, '//input[@id="agreement-checkbox-base"]')
t_write_name = (By.XPATH, '//input[@class="css-opa93d"]')
t_submit = (By.XPATH, '//button[@data-tests="submit-button"]')

cc_completion = (By.XPATH,
                 '//div[@class="rc-LoggedInHome-CourseCards css-53xei8"]/descendant::div[@data-testid="course-main-supplimentary-copy"][1]')

r_open_menu = (By.XPATH, '//button[@data-track-page="my_learning"][1]')
r_click_rate = (By.XPATH, '//li[@data-e2e="dropdown-option-rate-course"]')
r_rate_course = (By.XPATH, '//div[@class="rc-CourseRatingIcons rc-CourseRatingIconsAccessible large"]/child::label[6]')
r_click_submit = (By.XPATH, '//button[@data-e2e="SubmitButton"]')

rt_open_quiz_page = (By.XPATH, '//ul[@data-testid="named-item-list-list"]/descendant::p[@data-test="rc-ItemName"][3]')
rt_cont = (By.XPATH, '//button[@data-test="continue-button"]')
rt_try_again = (By.XPATH, '//a[@data-test="action-button"]/child::span[@class="cds-button-label"]')
rt_is_capable = (By.XPATH, '//div[@class="rc-FormPartsQuestion"]')
rt_resume = (By.XPATH, '//button[@aria-labelledby="Resume assignment"]')

vid_hover = (By.XPATH, '')
vid_pause = (By.XPATH, '//button[@class="rc-PlayToggle"]')
vid_play_off = (By.XPATH, '//div[@class="rc-VideoControlsContainer css-2lj8po"]/descendant::span[text()="Pause"]')

vid_mute = (By.XPATH, '//button[@aria-label="Mute"]')
vid_mute_on = (By.XPATH, '//video[@muted="muted"]')

vid_auto_p_on = (By.XPATH, '//button[@aria-label="Autoplay is on"]')
vid_auto_p_off = (By.XPATH, '//button[@aria-label="Autoplay is off"]')

vid_subs = (By.ID, 'subtitle-menu-button')
vid_no_subs = (By.XPATH, '//ul[@id="subtitle-menu"]/descendant::button[1]')
vid_sub2 = (By.XPATH, '//ul[@id="subtitle-menu"]/descendant::button[2]')
vid_check_on_subs1 = (By.XPATH,
                      '//ul[@id="subtitle-menu"]/descendant::button[1]/child::em[@class="cif-lg cif-fw c-subtitles-menu-item-selected-icon css-1oxiizq"]')
vid_check_on_subs2 = (By.XPATH,
                      '//ul[@id="subtitle-menu"]/descendant::button[2]/child::em[@class="cif-lg cif-fw c-subtitles-menu-item-selected-icon css-1oxiizq"]')
vid_check_off_subs1 = (By.XPATH,
                       '//ul[@id="subtitle-menu"]/descendant::button[1]/child::em[@class="cif-lg cif-fw c-subtitles-menu-item-selected-icon css-10pgxt2"]')
vid_check_off_subs2 = (By.XPATH,
                       '//ul[@id="subtitle-menu"]/descendant::button[2]/child::em[@class="cif-lg cif-fw c-subtitles-menu-item-selected-icon css-10pgxt2"]')

vid_settings = (
    By.XPATH, '//button[@class="vjs-menu-button vjs-menu-button-popup vjs-button vjs-control c-vjs-button"]')
vid_quality = (By.XPATH, '')

vid_playback = (By.XPATH, '')
vid_playback_1 = (By.XPATH, '//div[@class="rc-PlaybackRateChangeSection"]/descendant::button[@aria-label][1]')
vid_playback_2 = (By.XPATH, '//div[@class="rc-PlaybackRateChangeSection"]/descendant::button[@aria-label][2]')


vid_quality_1 = (By.XPATH, '//div[@class="rc-ResolutionChangeSection"]/descendant::button[@aria-label][1]')
vid_quality_2 = (By.XPATH, '//div[@class="rc-ResolutionChangeSection"]/descendant::button[@aria-label][2]')


nt_save_note = (By.XPATH, '//button[@data-track-component="create_video_highlight"]')
nt_course_home_page = (
    By.XPATH, '//nav[@aria-label="Primary breadcrumb"]/descendant::li[@class="cds-breadcrumbs-listItem"][1]')
nt_notes = (By.XPATH, '//li[@data-e2e="notesNavigationItem"]')
nt_saved_note = (By.XPATH, '//main[@id="main"]/descendant::div[@data-e2e="snapshot-container"][1]')
nt_timing_notes_video = (By.XPATH, '//div[@role="tabpanel"]/descendant::button[@aria-label][1]')
nt_timing_notes_save = (By.XPATH, '//p[@aria-label="Duration"]')
nt_timing_video = (By.XPATH,
                   '//div[@class="rc-VideoTimeDisplay horizontal-box align-items-absolute-center"]/child::span[@class="current-time-display"]')
nt_notes_video = (By.XPATH, '//div[@aria-label="Related lecture content tabs"]/descendant::button[2]')

nt_thgts_edit_notes = (By.XPATH, '//div[@data-e2e="note-card"]/descendant::button[1]')
nt_thgts_write = (By.ID, 'edit-note')
nt_thgts_save = (By.XPATH, '//div[@data-e2e="note-card"]/descendant::button[1]')
nt_thgts_check = (By.XPATH, '//p[@data-e2e="video-note-text"]')

nt_delete_note = (By.XPATH, '//div[@data-e2e="note-card"]/descendant::button[2]')
nt_confirm_delete = (By.XPATH, '//div[@data-e2e="note-card"]/descendant::button[1]')


class EnrollToCourse(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def open(self):
        return self.browser.get('https://www.coursera.org/')

    @allure.step('Enter text')
    def search_course(self):
        return self.find(e_search_text_area).send_keys('Business Analysis & Process Management')

    @allure.step('Click search')
    def click_search(self):
        return self.find(e_click_search).click()

    @allure.step('Click Course')
    def click_course(self):
        return self.find(e_click_course).click()

    @allure.step('Enroll to course')
    def enroll(self):
        focus_window = self.browser.window_handles
        self.browser.switch_to.window(focus_window[0])
        self.browser.close()
        self.browser.switch_to.window(focus_window[-1])
        return self.find(e_enroll).click()

    @allure.step('Continue the course')
    def click_continue(self):
        try:
            return self.find(e_click_continue).click()
        except NoSuchElementException:
            return True

    @allure.step('Close commitment window')
    def close_commit_window(self):
        try:
            return self.find(e_close_entry_window).click()
        except:
            return True

    @allure.step('Close goals window')
    def close_goals_window(self):
        return self.find(e_close_goals_window).click()


class CompleteCourse(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def open(self):
        return self.browser.get('https://www.coursera.org/my-learning?myLearningTab=IN_PROGRESS')

    def open_course(self):
        return self.find(c_open_course).click()

    def temp_open(self):
        return self.browser.get('https://www.coursera.org/learn/business-analysis-process-management/home/week/1')

    @allure.step('Watch introduction to course video')
    def watch_intro(self):
        #focus_window = self.browser.window_handles
        #self.browser.switch_to.window(focus_window[0])
        #self.browser.close()
        #self.browser.switch_to.window(focus_window[1])
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
        if len(focus_window) > 1:
            self.browser.switch_to.window(focus_window[2])
            self.browser.close()
        self.browser.switch_to.window(focus_window[1])
        self.browser.close()
        self.browser.switch_to.window(focus_window[0])
        sleep(5)

    @allure.step('Click quiz page')
    def click_quiz(self):
        return self.find(c_click_quiz).click()

    @allure.step('Click start quiz')
    def click_start_quiz(self):
        # self.find(t_cont).click()
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


class CourseCompletion(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def open(self):
        return self.browser.get('https://www.coursera.org/my-learning?myLearningTab=COMPLETED')

    def check_course_completion(self):
        return self.find(cc_completion).click()


class RateCourse(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def open(self):
        try:
            self.browser.get('https://www.coursera.org/my-learning?myLearningTab=COMPLETED')
            self.find(r_open_menu)
        except AssertionError:
            self.browser.get('https://www.coursera.org/my-learning?myLearningTab=IN_PROGRESS')
            self.find(r_open_menu)

    def open_menu(self):
        return self.find(r_open_menu).click()

    def click_rate(self):
        return self.find(r_click_rate).click()

    def rate_course(self):
        return self.find(r_rate_course)

    def submit_rating(self):
        return self.find(r_click_submit)


class RetakeTest(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def temp_open(self):
        return self.browser.get('https://www.coursera.org/learn/build-free-website-wordpress/home/week/1')

    def open_quiz(self):
        return self.find(rt_open_quiz_page).click()

    @allure.step('Continue the course')
    def click_continue(self):
        try:
            return self.find(rt_cont).click()
        except NoSuchElementException:
            return True

    def click_try_again(self):
        try:
            return self.find(rt_try_again).click()
        except NoSuchElementException:
            return self.find(rt_resume).click()

    def check_if_capable(self):
        return self.find(rt_is_capable)


class VideoPlayerCheck(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)
        self.playback1 = None
        self.playback2 = None
        self.quality1 = None
        self.quality2 = None

    @allure.step('Open main page')
    def temp_open(self):
        return self.browser.get(
            'https://www.coursera.org/learn/business-analysis-process-management/lecture/dOFt9/welcome-to-your-guided-project')

    @allure.step('Hover over player to show buttons')
    def hover(self):
        return self.browser.moveToElement(vid_hover).perform()

    @allure.step('Pause video')
    def click_pause(self):
        self.find(vid_pause).click()
        try:
            if self.find(vid_play_off):
                self.find(vid_pause).click()
        except NoSuchElementException:
            return True

    @allure.step('Mute video')
    def click_mute(self):
        self.find(vid_mute).click()
        if self.find(vid_mute_on):
            return True
        else:
            self.find(vid_mute).click()
            self.find(vid_mute).click()

    @allure.step('Click autoplay')
    def click_autoplay(self):
        sleep(2)
        try:
            if self.find(vid_auto_p_on):
                self.find(vid_mute_on).click()
            elif self.find(vid_play_off):
                self.find(vid_play_off).click()
        except ElementClickInterceptedException:
            return True

    @allure.step('Open settings meny')
    def click_settings(self):
        return self.find(vid_settings).click()

    @allure.step('Open subtitles menu')
    def click_subs(self):
        return self.find(vid_subs).click()

    @allure.step('Turn off subtitles')
    def turn_off_subs(self):
        return self.find(vid_no_subs).click()

    @allure.step('Turn on first available subtitles')
    def turn_on_subs1(self):
        return self.find(vid_sub2).click()

    @allure.step('Check subtitles')
    def check_subs(self):
        try:
            self.find(vid_check_on_subs1)
        except NoSuchElementException:
            return self.find(vid_check_on_subs2)

    @allure.step('Find playback to lower it')
    def playback_assertion_1(self):
        return self.find(vid_playback_1)

    @allure.step('Find playback to increase it')
    def playback_assertion_2(self):
        return self.find(vid_playback_2)

    @allure.step('Change playback options')
    def playback_to_click_check(self):
        self.playback1 = self.playback_assertion_1()
        playback1 = self.playback1.get_attribute('aria-label')
        self.playback2 = self.playback_assertion_2()
        playback2 = self.playback2.get_attribute('aria-label')
        print(playback2)
        print(playback1)
        if playback1 == 'decrease playback rate to 0.75' and playback2 == 'increase playback rate to 1.25':
            self.find(vid_playback_1).click()
            print(playback1)
        elif playback2 == ('increase playback rate to 1'):
            self.find(vid_playback_2).click()
            print(playback2)

    @allure.step('Find quality to lower it')
    def quality_assertion_1(self):
        return self.find(vid_quality_1)

    @allure.step('Find quality to increase it')
    def quality_assertion_2(self):
        return self.find(vid_quality_2)

    @allure.step('Change quality options')
    def quality_to_assert(self):
        self.quality1 = self.quality_assertion_1()
        quality1 = self.quality1.get_attribute('aria-label')
        self.quality2 = self.quality_assertion_2()
        quality2 = self.quality2.get_attribute('aria-label')
        print(quality1)
        print(quality2)
        if quality1 == 'decrease video quality to 240p' and quality2 == 'increase video quality to 540p':
            self.find(vid_playback_1).click()
            print(quality1)
        elif quality2 == 'increase video quality to 720p':
            self.find(vid_playback_2).click()
            print(quality2)


class SavingNotesCheck(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)
        self.timing_vid_nt = None
        self.timing_nt_save = None
        self.timing_vid = None

    @allure.step('Open main page')
    def temp_open(self):
        return self.browser.get(
            'https://www.coursera.org/learn/business-analysis-process-management/lecture/dOFt9/welcome-to-your-guided-project')

    @allure.step('Save a note on the video')
    def click_save_note(self):
        return self.find(nt_save_note).click()

    @allure.step('Check timings of the video')
    def check_video_notes_timing(self):
        self.find(v_click_notes_in_video).click()
        return self.find(nt_timing_notes_video)

    @allure.step('Save the timing')
    def save_video_notes_timing(self):
        self.timing_vid_nt = self.check_video_notes_timing()
        return self.timing_vid_nt

    @allure.step('Open course main page')
    def click_course_homepage(self):
        return self.find(nt_course_home_page).click()

    @allure.step('Open notes')
    def click_notes(self):
        return self.find(nt_notes).click()

    @allure.step('Check timing in the notes')
    def check_saved_notes_timing(self):
        return self.find(nt_timing_notes_save)

    @allure.step('Save timing in the notes')
    def save_notes_saved_timing(self):
        self.timing_nt_save = self.check_saved_notes_timing()
        return self.timing_nt_save

    @allure.step('Open created note')
    def open_note(self):
        self.find(nt_saved_note).click()

    def click_notes_video(self):
        return self.find(nt_notes_video).click()

    @allure.step('Check opened timing in the notes')
    def check_video_timing(self):
        focus_window = self.browser.window_handles
        self.browser.switch_to.window(focus_window[1])
        return self.find(nt_timing_video)

    @allure.step('Save video timing')
    def save_video_timing(self):
        self.timing_vid = self.check_video_timing()
        return self.timing_vid

    @allure.step('Check if saved timings of the note correspond to the one opened')
    def timing_check(self):
        timing_vid_nt = self.timing_nt_save().get_attribute('@aria-label')
        timing_nt_save = self.save_video_timing.text
        timing_vid = self.check_video_timing.text

        print(timing_vid, timing_vid_nt, timing_nt_save)


class DeleteNotes(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)
        self.timing_vid_nt = None
        self.timing_nt_save = None
        self.timing_vid = None

    @allure.step('Open main page')
    def temp_open(self):
        return self.browser.get(
            'https://www.coursera.org/learn/business-analysis-process-management/lecture/dOFt9/welcome-to-your-guided-project')

    @allure.step('Save a note')
    def click_save_note(self):
        return self.find(nt_save_note).click()

    @allure.step('Open course main page')
    def click_course_homepage(self):
        return self.find(nt_course_home_page).click()

    @allure.step('Open notes')
    def click_notes(self):
        return self.find(nt_notes).click()

    @allure.step('Click delete note')
    def click_delete(self):
        return self.find(nt_delete_note).click()

    @allure.step('Confirm deletion')
    def click_confirm_delete(self):
        return self.find(nt_confirm_delete).click()


class AddThoughts(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def temp_open(self):
        return self.browser.get(
            'https://www.coursera.org/learn/business-analysis-process-management/lecture/dOFt9/welcome-to-your-guided-project')

    @allure.step('Create a note')
    def click_save_note(self):
        return self.find(nt_save_note).click()

    @allure.step('Open course main page')
    def click_course_homepage(self):
        return self.find(nt_course_home_page).click()

    @allure.step('Open notes')
    def click_notes(self):
        return self.find(nt_notes).click()

    @allure.step('Open textbox to add description to the note')
    def click_edit_thoughts(self):
        return self.find(nt_thgts_edit_notes).click()

    @allure.step('Add description to the note')
    def add_thoughts(self):
        return self.find(nt_thgts_write).send_keys("asd")

    @allure.step('Save description')
    def save_thoughts(self):
        return self.find(nt_thgts_save).click()

    @allure.step('Check the description')
    def check_added_thoughts(self):
        return self.find(nt_thgts_check)
