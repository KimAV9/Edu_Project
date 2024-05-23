from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random
from time import sleep
import allure

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
p_create_option1 = (By.XPATH, '//div[@role="listbox"]')
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

    @allure.step('OPen main page')
    def open_page(self):
        return self.browser.get('https://www.coursera.org/')

    @allure.step('Open registration page')
    def register(self):
        return self.find(register).click()

    @allure.step('Write full name')
    def register_fullname(self):
        self.find(register_fullname).click()
        return self.find(register_fullname).send_keys(name)

    @allure.step('Write password')
    def register_password(self):
        self.find(register_password).click()
        print(password)
        return self.find(register_password).send_keys(password)

    @allure.step('Get temporary email')
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

    @allure.step('Click register')
    def register_button(self):
        return self.find(register_button).click()

    @allure.step('Click forgot password')
    def forgot_password(self):
        self.browser.get('https://www.coursera.org/?authMode=login')
        return self.find(forgot_password).click()

    @allure.step('Enter registered email')
    def enter_email(self):
        return self.find(forgot_email).send_keys('nolim60871@picdv.com')

    @allure.step('Click reset password')
    def click_reset_password(self):
        return self.find(reset_password).click()


class Background(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_page(self):
        return self.browser.get('https://www.coursera.org/?isNewUser=true&showOnboardingModal=1/')

    @allure.step('Write a work occupation')
    def write_work_occup(self):
        self.find(p_w_occupation).send_keys(name)
        return self.find(p_create_option1).click()

    @allure.step('Click work experience menu')
    def click_work_exp(self):
        return self.find(p_click_exp_level).click()

    @allure.step('Choose work experience from the list')
    def choose_exp(self):
        return self.find(p_choose_exp_level).click()

    @allure.step('Write an employer')
    def write_employer(self):
        self.find(p_employer).send_keys(name)
        return self.find(p_create_option1).click()

    @allure.step('Click "I currently work here" checkmark')
    def click_work_now(self):
        return self.find(p_work_now).click()

    @allure.step('Open degree menu')
    def click_degree(self):
        return self.find(p_click_degree).click()

    @allure.step('Choose a higher education degree')
    def choose_degree(self):
        return self.find(p_choose_degree).click()

    @allure.step('Write a name of the university')
    def write_uni(self):
        self.find(p_uni).send_keys(name)
        return self.find(p_create_option1).click()

    @allure.step('Open major menu')
    def click_field(self):
        return self.find(p_click_field).click()

    @allure.step('Choose major')
    def choose_field(self):
        return self.find(p_choose_field).click()

    @allure.step('Click "I am currently studying here" checkbox')
    def click_study_now(self):
        return self.find(p_now_student).click()

    @allure.step('Write your occupational goal')
    def write_goal_occup(self):
        self.find(p_cg_occupation).send_keys(name)
        return self.find(p_create_option1).click()

    @allure.step('Write in which industry is that goal')
    def write_industry(self):
        self.find(p_industry).send_keys(name)
        return self.find(p_create_option1).click()

    @allure.step('Save changes')
    def click_cont(self):
        return self.find(p_continue).click()
