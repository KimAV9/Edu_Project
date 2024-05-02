from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random
import pyperclip
from time import sleep

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


class RandomGenerator:
    def __init__(self, min_length=4, max_length=10):
        self.vowels = "aeiou"
        self.consonants = "bcdghjklmnpqrstvwxyz"
        self.numbers = "0123456789"
        self.min_length = min_length
        self.max_length = max_length

    def generate_name(self):
        length = random.randint(self.min_length, self.max_length)
        gen_name = "".join(random.choice(self.consonants + self.vowels) for x in range(length))
        return gen_name.capitalize()

    def generate_password(self):
        length = random.randint(8, 12)
        gen_password = "".join(random.choice(self.consonants + self.vowels + self.numbers) for x in range(length))
        print(gen_password)
        return gen_password


name = RandomGenerator().generate_name()
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
