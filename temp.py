from selenium.webdriver.common.by import By
import random
import allure


c_watch = (By.XPATH, '//button[@class="cds-105 cds-button-disableElevation cds-button-primary css-ra3hwj"]')
mark_complete = (By.XPATH, '//button[@data-testid="mark-complete"]')
read_comm_disc =(By.XPATH, '//div[@class="item-tools-and-content-container"]/descendant::a[@data-testid="learner-app-client-navigation-link"][3]')
open_lab= (By.XPATH, '//main[@id="main"]//descendant::button[@data-track-app="open_course_home"]')
how_want_to_learn_open = (By.XPATH, '//div/descendant::button[@aria-describedby="byob-mode-description"][1]')
lab_instructions_close = (By.XPATH, '//section[@aria-label="Instructions"]/descendant::button[1]')


from pypasser import reCaptchaV2

@allure.step('Click login button')
def login_button(self):
    self.find(login_button).click()
    is_checked = reCaptchaV2(driver=self.browser, play=False)
    if is_checked:
        # Click submit button
        self.find(captcha).click()
        if 'Verification Success' in self.browser.page_source:
            print('SUCCESS')

    else:
        print('FAIL')