from selenium.webdriver.common.by import By
import random

class Account():
    select_account = '//ul[@role="menu"]/descendant::li[@class="css-o9b79t"][1]'
    fullname_field = (By.ID, 'settings-basic-full-name')
    email_field = (By.ID, 'settings-basic-email')

    timezone_menu = (By.ID, 'settings-basic-timezone')
    timezone_select = f'//select[@name="timezone"]/descendant::option[{random.randint(1,417)}]'

    language_menu = (By.ID, 'settings-basic-language')
    lang_select = f'//select[@name="locale"]/descendant::option[{random.randint(2,24)}]'

    save_button = [By.XPATH, '//div[@class="rc-BasicInformation"]//child::span[@class="cds-button-label"]']

    current_password_field = (By.ID, 'settings-password-current')
    new_password_field = (By.ID, 'settings-password-new')
    confirm_password_field = (By.ID, 'settings-password-new-confirm')

    delete_button = (By.XPATH, '//button[@class="secondary cozy settings-primary-action"]')

class CommPref():
    select_commpref = '//ul[@role="menu"]/descendant::li[@class="css-o9b79t"][2]'

    opt_out = '//div[@class="rc-EmailPreferences"]/descendant::label[@class="cds-checkboxAndRadio-label"][1]'
    weekly_pers_recom = '//div[@class="rc-EmailPreferences"]/descendant::label[@class="cds-checkboxAndRadio-label"][2]'
    weekly_notif = '//div[@class="rc-EmailPreferences"]/descendant::label[@class="cds-checkboxAndRadio-label"][3]'
    info_on_degree = '//div[@class="rc-EmailPreferences"]/descendant::label[@class="cds-checkboxAndRadio-label"][4]'
    surveys = '//div[@class="rc-EmailPreferences"]/descendant::label[@class="cds-checkboxAndRadio-label"][5]'
    save_coursear_comms = '//div[@class="rc-EmailPreferences"]/descendant::button[@class="secondary cozy settings-primary-action"][1]'

    course_announce = '//div[@class="rc-EmailPreferences"]/descendant::div[@class="preference-item"][1]'
    course_remidnder = '//div[@class="rc-EmailPreferences"]/descendant::div[@class="preference-item"][2]'
    course_discuss = '//div[@class="rc-EmailPreferences"]/descendant::div[@class="preference-item"][3]'
    save_course_cooms = '//div[@class="rc-EmailPreferences"]/descendant::button[@class="secondary cozy settings-primary-action"][2]'

    comms_partner_1 = '//div[@class="rc-EmailPreferences"]/descendant::label[@class="preference-item"][1]'
    comms_partner_2 = '//div[@class="rc-EmailPreferences"]/descendant::label[@class="preference-item"][2]'
    save_partners_comms = '//div[@class="rc-EmailPreferences"]/descendant::button[@class="secondary cozy settings-primary-action"][3]'


class NoteAndHigh():
    select_note = '//ul[@role="menu"]/descendant::li[@class="css-o9b79t"][3]'

class Calendar():
    select_calendar = '//ul[@role="menu"]/descendant::li[@class="css-o9b79t"][4]'


class Randomizer():
    def __init__(self, browser):
        super().__init__(browser)

    def timezone_randomizer(self):
        afirca = [By.XPATH, f'//optgroup [@label="Africa"]/child::option[@value!="UTC"][{random.randint(1, 52)}]']
        timezone_numbers = random.randint(1, 11)
        if timezone_numbers == 1:
            self.find()
timezone = [By.XPATH, '//select [@id="settings-basic-timezone"]/child::optgroup[@label!=""][]']