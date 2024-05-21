from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random
import pyperclip
from time import sleep
from keyboard import press

register = (By.XPATH, '//a[@class="standardSignupBtnLink signup-jff-fp-btn link-button primary"]')
register_fullname = (By.ID, 'name')
register_email = (By.ID, 'email')
register_password = (By.ID, 'password')
register_button = (By.XPATH, '//button[@class="_6dgzsvq css-j6v0dd"]')
copy_mail = (By.XPATH, '//button[@class="btn-rds icon-btn bg-theme click-to-copy copyIconGreenBtn"]')
wait_for_mail = (By.XPATH, '//input[@class="emailbox-input opentip')
forgot_password = (By.XPATH, '//button[@class="_eweitj" and text() ="Forgot password?"]')
forgot_email = (By.XPATH, '//input[@class="css-xvsivy"]')
reset_password = (By.XPATH, '//button[@class="css-1deqff9"]')

p_w_occupation = (By.ID, 'OccupationsDropdown~workExp')
p_click_exp_level = (By.ID, 'current_occupation_level')
p_choose_exp_level = (By.XPATH, f'//select[@id="current_occupation_level"]/child::option[{random.randint(2, 8)}]')
p_employer = (By.ID, 'CompanyDropdown~workExp')
p_work_now = (By.ID, 'trackedEmployerCheckbox')
p_click_degree = (By.ID, 'educational_attainment')
p_choose_degree = (By.XPATH, f'//select[@id="educational_attainment"]/child::option[{random.randint(2, 8)}]')
p_uni = (By.ID, 'university_dropdown')
p_click_field = (By.ID, 'education_major')
p_choose_field = (By.XPATH, f'//select[@id="education_major"]/child::option[{random.randint(2, 14)}]')
p_now_student = (By.XPATH, '//input[@data-track-component="current_student_checkbox"]')
p_cg_occupation = (By.ID, 'OccupationsDropdown~goals')
p_industry = (By.ID, 'IndustriesDropdown~careerGoal')
p_continue = (By.XPATH, '//button[@data-track-component="onboarding_continue_button"]')


class RandomGenerator:
    def __init__(self, min_length=4, max_length=10):
        self.vowels = "aeiou"
        self.consonants = "bcdghjklmnpqrstvwxyz"
        self.numbers = "0123456789"
        self.min_length = min_length
        self.max_length = max_length

    def generate_text(self):
        length = random.randint(self.min_length, self.max_length)
        gen_name = "".join(random.choice(self.consonants + self.vowels) for x in range(length))
        return gen_name.capitalize()

    def generate_password(self):
        length = random.randint(8, 12)
        gen_password = "".join(random.choice(self.consonants + self.vowels + self.numbers) for x in range(length))
        print(gen_password)
        return gen_password

    def generate_email(self):
        return self.generate_text() + ('@cats.meows')


name = RandomGenerator().generate_text()
password = RandomGenerator().generate_password()


class RegistrationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_page(self):
        return self.browser.get('https://www.coursera.org/')

    def register(self):
        return self.find(register).click()

    def register_fullname(self):
        self.find(register_fullname).click()
        return self.find(register_fullname).send_keys(name)

    def register_password(self):
        self.find(register_password).click()
        print(password)
        return self.find(register_password).send_keys(password)

    def register_email(self):
        # self.browser.switch_to.new_window('tab')
        # self.browser.get('https://temp-mail.org/ru/')
        # sleep(5)
        # self.find(wait_for_mail)
        # self.find(copy_mail).click()
        # self.browser.switch_to.window(self.browser.window_handles[0])
        # self.find(register_email).click()//
        # return self.find(register_email).send_keys(f'{pyperclip.paste()}')
        return self.find(register_email).send_keys('nolim60871@picdv.com')

    def register_button(self):
        return self.find(register_button).click()

    def forgot_password(self):
        self.browser.get('https://www.coursera.org/?authMode=login')
        return self.find(forgot_password).click()

    def enter_email(self):
        return self.find(forgot_email).send_keys('nolim60871@picdv.com')

    def click_reset_password(self):
        return self.find(reset_password).click()


class Background(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_page(self):
        return self.browser.get('https://www.coursera.org/?isNewUser=true&showOnboardingModal=1/')

    def write_work_occup(self):
        self.find(p_w_occupation).send_keys(name)
        return press('enter')

    def click_work_exp(self):
        return self.find(p_click_exp_level).click()

    def choose_exp(self):
        return self.find((p_choose_exp_level)).click()

    def write_employer(self):
        self.find(p_employer).send_keys(name)
        return press('enter')

    def click_work_now(self):
        return self.find(p_work_now).click()

    def click_degree(self):
        return self.find(p_click_degree).click()

    def write_uni(self):
        self.find(p_uni).send_keys(name)
        return press('enter')

    def click_field(self):
        return self.find(p_click_field).click()

    def choose_field(self):
        return self.find(p_choose_field).click()

    def click_study_now(self):
        return self.find(p_now_student).click()

    def write_goal_occup(self):
        self.find(p_cg_occupation)
        return press('enter')

    def write_industry(self):
        self.find(p_industry)
        return press('enter')

    def click_cont(self):
        return self.find(p_continue)
