from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from pages.registration_page import password
import random
import allure


c_prof_menu = (By.XPATH, '//button[@data-track-component="profile_drop_down_btn"]')
c_profile = (By.XPATH, '//div[@class="header-right-nav-wrapper css-1h9ktwj"]/descendant::li[@role="menuitem"][11]')

text = ('Groovy')
#text = RandomGenerator.generate_text()
x = random.randint(1, 12)
y = x - 1

w_add_work_exp = (By.XPATH, '//div[@class="cds-9 css-dv86ch cds-10 cds-18 cds-29"]/descendant::button[@class ="cds-149 cds-button-disableElevation cds-button-secondary css-1pddt1l"]')

w_name_of_inst = (By.XPATH, '//span[@class="fs-mask"]/descendant::button[@class="css-1sifyul"]')
w_add_name_of_inst = '//div[@class="menu-item-inactive css-1bol722"]'
w_text_inst = (By.XPATH, '//span[@data-e2e="profile-work-institution"]/descendant::p[text()=""]')

create_item = (By.XPATH, '//button[@class ="cds-149 cds-button-disableElevation cds-button-ghost css-htiquy"]')
delete_text = (By.XPATH, '//div[@class ="css-vu83vx"]')
close = (By.XPATH, '//button[@class="cds-149 cds-button-disableElevation cds-button-ghost css-1s96oj"]')

w_role = (By.XPATH, f'//div[@class="menu-item-inactive css-1bol722"][{random.randint(1, 100)}]')
w_add_role = (By.XPATH, '//div[@data-e2e="profile-work-role"]')
w_text_role = (By.XPATH, '//div[@data-e2e="profile-work-role"]/descendant::p[text()=""]]')

w_start_month = (By.XPATH,
                 '//div[@data-e2e= "profile-work-start"]/descendant::div[@class = "cds-204 cds-205 cds-select-select cds-208 cds-241 cds-225 cds-input-input"][1]')
w_add_start_month = (By.XPATH,
                     f'//li[@class ="cds-149 cds-1564 cds-1560 cds-selectOption-root css-xzdz7m cds-1561 cds-1571 cds-1572 cds-selectOption-button"][{random.randint(1, 12)}]')

w_start_year = (By.XPATH,
                '//div[@data-e2e= "profile-work-start"]/descendant::div[@class = "cds-204 cds-205 cds-select-select cds-208 cds-241 cds-225 cds-input-input"][2]')
w_add_start_year = (By.XPATH,
                    f'//li[@class ="cds-149 cds-1611 cds-1607 cds-selectOption-root css-xzdz7m cds-1609 cds-selectOption-selected cds-1608 cds-1618 cds-1619 cds-selectOption-button cds-1621"][{y}]')

w_end_month = (By.XPATH,
               '//div[@data-e2e= "profile-work-end"]/descendant::div[@class = "cds-204 cds-205 cds-select-select cds-208 cds-241 cds-225 cds-input-input"][1]')
w_add_end_month = (By.XPATH,
                   '//li[@class="cds-149 cds-1748 cds-1744 cds-selectOption-root css-xzdz7m cds-1745 cds-1755 cds-1756 cds-selectOption-button"]')

w_end_year = (By.XPATH,
              '//div[@data-e2e= "profile-work-end"]/descendant::div[@class = "cds-204 cds-205 cds-select-select cds-208 cds-241 cds-225 cds-input-input"][2]')
w_add_end_year = (By.XPATH,
                  f'//li[@class="cds-149 cds-1842 cds-1838 cds-selectOption-root css-xzdz7m cds-1839 cds-1849 cds-1850 cds-selectOption-button"][{x}]')

w_still_work = (By.XPATH, '//label[@class="cds-checkboxAndRadio-label"]')
w_still_work_locked = (By.XPATH,
                       '//div[@class="cds-1899 cds-1900 cds-select-select cds-select-readOnly cds-1903 cds-1936 cds-1920 cds-input-input"]')

w_description = (By.XPATH, '//div[@data-e2e="profile-work-description"]/child::textarea[1]')

w_save = (By.XPATH, '//button[@data-e2e="profile-work-save"]')
w_remove = (By.XPATH, '//button[@data-track-component="profile_remove_work_history"]')

e_edu = (By.XPATH, '//button[@data-e2e="profile-education-section-add"]')
e_name_of_inst = (By.XPATH, '//button[@class="css-1sifyul"]')
e_add_name_of_inst = (By.XPATH, f'//div[@class="menu-item-inactive css-1bol722"][{random.randint(1, 10)}]')

e_degree = (By.XPATH, '//div[@data-e2e= "profile-education-degree"]/descendant::div[@class = "cds-438 cds-439 cds-select-select cds-442 cds-475 cds-459 cds-input-input"]')
e_add_degree = (By.XPATH, f'//li[@class="cds-149 cds-3472 cds-3468 cds-selectOption-root css-xzdz7m cds-3469 cds-3479 cds-3480 cds-selectOption-button"][{random.randint(3, 7)}]')

e_discipline = (By.XPATH, '//div[@data-e2e="profile-education-discipline"]/descendant::div[@class="cds-438 cds-439 cds-select-select cds-442 cds-475 cds-459 cds-input-input"]')
e_add_discipline = (By.XPATH, f'//li[@class="cds-149 cds-4365 cds-4361 cds-selectOption-root css-xzdz7m cds-4362 cds-4372 cds-4373 cds-selectOption-button"][{random.randint(1, 12)}]')
e_area_of_conc = (By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div[2]/div/div/div[4]/div[1]/fieldset')

e_start_month = (By.XPATH, '//div[@data-e2e= "profile-education-start-date"]/descendant::div[@class = "cds-464 cds-449 cds-input-root cds-input-onLight cds-select-field-root css-nuguie cds-465"][1]')
e_add_start_month = (By.XPATH, f'//li[@class ="cds-149 cds-4412 cds-4408 cds-selectOption-root css-xzdz7m cds-4409 cds-4419 cds-4420 cds-selectOption-button"][{random.randint(1, 12)}]')

e_start_year = (By.XPATH, '//div[@data-e2e= "profile-education-start-date"]/descendant::div[@class = "cds-464 cds-449 cds-input-root cds-input-onLight cds-select-field-root css-nuguie cds-465"][2]')
e_add_start_year = (By.XPATH, f'//li[@class ="cds-149 cds-4553 cds-4549 cds-selectOption-root css-xzdz7m cds-4550 cds-4560 cds-4561 cds-selectOption-button"][{y}]')

e_end_month = (By.XPATH, '//div[@data-e2e= "profile-education-end-date"]/descendant::div[@class = "cds-464 cds-449 cds-input-root cds-input-onLight cds-select-field-root css-nuguie cds-465"][1]')
e_add_end_month = (By.XPATH, '//li[@class="cds-149 cds-4506 cds-4502 cds-selectOption-root css-xzdz7m cds-4504 cds-selectOption-selected cds-4503 cds-4513 cds-4514 cds-selectOption-button cds-4516"]')

e_end_year = (By.XPATH, '//div[@data-e2e= "profile-education-end-date"]/descendant::div[@class = "cds-464 cds-449 cds-input-root cds-input-onLight cds-select-field-root css-nuguie cds-465"][2]')
e_add_end_year = (By.XPATH, f'//li[@class="cds-149 cds-4600 cds-4596 cds-selectOption-root css-xzdz7m cds-4597 cds-4607 cds-4608 cds-selectOption-button"][{x}]')

e_currently_study =(By.XPATH, '//label[@class="cds-checkboxAndRadio-label"]')
e_grade = (By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div[2]/div/div/div[8]/div/fieldset")

e_save = (By.XPATH, '//button[@data-track-component="profile_save_education_history"]')

i_add = (By.XPATH, '//section[@class="css-1gqjnbp"]/descendant::button[@data-track-component="profile_add_work_preferences"]')
i_about = (By.XPATH, '//div[@class="cds-687 cds-672 cds-input-root cds-text-field-root cds-input-onLight css-pphb6b cds-697 cds-688 cds-695 cds-680 cds-input-multiline"]/child::textarea[1]')
i_save = (By.XPATH, '//button[@data-track-component="profile_additional_info_save"]')

wp_dropdown_menu = (By.XPATH, '/*[name()="svg" and @data-testid = "icon-not-active"]')  # still udner work

wp_add_work_pref = (By.XPATH, '//span[@data-e2e="profile-desktop-panel"]/descendant::button[@data-e2e="profile-work-pref-edit"] [1]')
wp_delete_role = (By.XPATH, '//button[@data-testid="delete-role-preference-button"]')
wp_create_item = (By.XPATH, '//button[@class ="cds-149 cds-button-disableElevation cds-button-ghost css-1dab2db"]')

wp_add_role = (By.XPATH, '//div[@data-e2e="profile_edit_role"]/descendant::*[@class="css-1sifyul"][1]')
wp_choose_role = (By.XPATH, '//div[@class="css-1vxrzat"]/descendant::div[3]')
wp_add_industry = (By.XPATH, '//div[@data-e2e="profile_edit_role"]/descendant::*[@class="css-1sifyul"][2]')
wp_choose_industry = (By.XPATH, '//div[@class="css-1vxrzat"]/descendant::div[3]')
wp_add_another_role = (By.XPATH, '//button[@data-track-component="profile_add_work_preferences_role"]')

wp_save = (By.XPATH, '//button[@data-track-component="profile_save_work_preferences"]')

wp_add_role2 = ''  # underconstruction
wp_add_industry2 = ''

v_share_link = (By.XPATH, '//section[@data-e2e="profile-photo-and-invitation-section"]/descendant::button[3]')
v_copy_link = (By.XPATH, '//div[@data-track-component="profile_share_public_profile_dialog"]/descendant::button[1]')

v_customize_link = (By.XPATH, '//div[@data-track-component="profile_share_public_profile_dialog"]/descendant::button[2]')
v_enter_customization = (By.XPATH, '//input[@aria-label="Profile Link"]')
v_save_custom = (By.XPATH, '//button[@class="cds-149 cds-button-disableElevation cds-button-primary css-ra3hwj"]')
v_cancel_custom = (By.XPATH,
                   '//div[@class="css-1hllf5q"]/descendant::button[@class="cds-149 cds-button-disableElevation cds-button-ghost css-l0otf2"][1]')
v_got_it_btn = (By.XPATH, '//button[@data-e2e="share-profile-got-it"]')

v_update_visibility = (By.XPATH, '//section[@data-e2e="profile-photo-and-invitation-section"]/descendant::button[4]')
v_anyone_with_link = (By.XPATH, '//label[@class="cds-checkboxAndRadio-label"]')
v_done = (By.XPATH, '//button[@class="cds-149 cds-button-disableElevation cds-button-primary css-ra3hwj"]')

ed_edit_btn = (By.XPATH, '//button[@data-e2e="profile_edit_intro_profile"]')
ed_edit_name = (By.XPATH, '//input[@name="fullName"]')
ed_edit_pronoun = (By.XPATH, '//input[@name="pronoun"]')

ed_edit_gender = (By.XPATH, '//div[@class="cds-1038 cds-1039 cds-select-select cds-1042 cds-1027 cds-1011 cds-input-input"]')
ed_choose_gender = (By.XPATH, f'//ul[@class="cds-1175 cds-1050 cds-select-list cds-1176"]/child::li[{random.randint(1, 8)}]')
ed_save = (By.XPATH, '//button[@data-track-component="profile_save_intro_profile"]')


class ProfilePage(AuthPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Open main page')
    def open2(self):
        return self.main_page()

    @allure.step('Login')
    def login2(self):
        self.login()
        self.login_email()
        self.login_password()
        return self.login_button()

    @allure.step('Open account menu')
    def p_open_prof_menu(self):
        return self.find(c_prof_menu).click()

    @allure.step('Open settings page')
    def p_open_profile(self):
        return self.find(c_profile).click()

    @allure.step('Click on add work experience')
    def w2_add_work_exp(self):
        return self.find(w_add_work_exp).click()

    @allure.step('Click on select institution in work experience')
    def w2_click_name_of_inst(self):
        return self.find(w_name_of_inst).click()

    @allure.step('Select institution in work experience')
    def w2_choose_name_of_inst(self):
        return self.find(w_add_name_of_inst).click()

    @allure.step('Click on select role in work experience')
    def w2_click_role(self):
        return self.find(w_role).click()

    @allure.step('Choose role in work experience')
    def w2_choose_role(self):
        return self.find(w_add_role).click()

    @allure.step('Click select start date month in work experience')
    def w2_start_month(self):
        return self.find(w_start_month).click()

    @allure.step('Choose select start date month in work experience')
    def w2_start_choose_month(self):
        return self.find(w_add_start_month).click()

    @allure.step('Click select start date year in work experience')
    def w2_start_year(self):
        return self.find(w_start_year).click()

    @allure.step('Choose select start date year in work experience')
    def w2_start_choose_year(self):
        return self.find(w_add_start_year).click()

    @allure.step('Click select end date month in work experience')
    def w2_end_month(self):
        return self.find(w_end_month).click()

    @allure.step('Choose select end date month in work experience')
    def w2_end_choose_month(self):
        return self.find(w_add_end_month).click()

    @allure.step('Click select end date year in work experience')
    def w2_end_year(self):
        return self.find(w_end_year).click()

    @allure.step('Choose select end date year in work experience')
    def w2_end_choose_year(self):
        return self.find(w_add_end_year).click()

    @allure.step('Click checkbox "I currently work here"')
    def w2_current_work(self):
        return self.find(w_still_work).click()

    @allure.step('Check if end date is blocked')
    def w2_end_date_block(self):
        return self.find(w_still_work_locked)

    @allure.step('Add description')
    def w2_add_description(self):
        return self.find(w_description).send_keys(text)

    @allure.step('Save changes in work experience')
    def w2_save(self):
        return self.find(w_save).click()

    @allure.step('Click add education')
    def e2_add_edu(self):
        return self.find(e_edu).click()

    @allure.step('Click select institution in education')
    def e2_name_of_inst(self):
        return self.find(e_name_of_inst).click()

    @allure.step('Select name of institution in education')
    def e2_choose_inst(self):
        return self.find(e_add_name_of_inst).click()

    @allure.step('Click select degree in education')
    def e2_degree(self):
        return self.find(e_degree).click()

    @allure.step('Choose degree in education')
    def e2_choose_degree(self):
        return self.find(e_add_degree).click()

    @allure.step('Click select discipline')
    def e2_discipline(self):
        return self.find(e_discipline).click()

    @allure.step('Choose discipline')
    def e2_choose_discipline(self):
        return self.find(e_add_discipline).click()

    @allure.step('Write a text in area of concentration')
    def e2_area_of_conc(self):
        return self.find(e_area_of_conc).send_keys(text)

    @allure.step('Click start date month in education')
    def e2_start_month(self):
        return self.find(e_start_month).click()

    @allure.step('Choose start date month in education')
    def e2_start_choose_month(self):
        return self.find(e_add_start_month).click()

    @allure.step('Click start date year in education')
    def e2_start_year(self):
        return self.find(e_start_year).click()

    @allure.step('Choose start date year in education')
    def e2_start_choose_year(self):
        return self.find(e_add_start_year).click()

    @allure.step('Click end date month in education')
    def e2_end_month(self):
        return self.find(e_end_month).click()

    @allure.step('Choose end date month in education')
    def e2_end_choose_month(self):
        return self.find(e_add_end_month).click()

    @allure.step('Click end date year in education')
    def e2_end_year(self):
        return self.find(e_end_year).click()

    @allure.step('Choose end date year in education')
    def e2_end_choose_year(self):
        return self.find(e_add_end_year).click()

    @allure.step('Click checkbox "I currently study here"')
    def e2_currently_study(self):
        return self.find(e_currently_study).click()

    @allure.step('Enter text in field of "Cumulative Grade"')
    def e2_cumulative_grade(self):
        return self.find(e_grade).send_Keys(text)

    @allure.step('Click save in education')
    def e2_save(self):
        return self.find(e_save).click()

    @allure.step('Click add work preferences')
    def wp2_work_pref(self):
        return self.find(wp_add_work_pref).click()

    @allure.step('Click role in work preferences')
    def wp2_role(self):
        return self.find(wp_add_role).click()

    @allure.step('Choose role in work preferences')
    def wp2_choose_role(self):
        return self.find(wp_choose_role).click()

    @allure.step('Click industry in work preferences')
    def wp2_industry(self):
        return self.find(wp_add_industry).click()

    @allure.step('Choose industry in work preferences')
    def wp2_choose_industry(self):
        return self.find(wp_choose_industry).click()

    @allure.step('Click save in work preferences')
    def wp2_save(self):
        return self.find(wp_save).click()

    @allure.step('Click add additional info')
    def i2_add_info(self):
        return self.find(i_add).click()

    @allure.step('Add text in about field')
    def i2_write_about(self):
        return self.find(i_about).send_keys(text)

    @allure.step('Click save in additional info')
    def i2_save(self):
        return self.find(i_save).click()

    @allure.step('Click update profile visibility')
    def v2_udt_vis(self):
        return self.find(v_update_visibility)

    @allure.step('Click on checkbox anyone with a link')
    def v2_who_sees(self):
        return self.find(v_anyone_with_link).click()

    @allure.step('Click done')
    def v2_done(self):
        return self.find(v_done).click()

    @allure.step('Click edit button')
    def ed2_edit(self):
        return self.find(ed_edit_btn).click()

    @allure.step('Enter text in first and last name ')
    def ed2_name(self):
        return self.find(ed_edit_name).send_keys(text)

    @allure.step('Enter text in pronouns')
    def ed2_pronouns(self):
        return self.find(ed_edit_pronoun).send_keys(text)

    @allure.step('Click choose gender')
    def ed2_gender(self):
        return self.find(ed_edit_gender).click()

    @allure.step('Choose gender')
    def ed2_choose_gender(self):
        return self.find(ed_choose_gender).click()

    @allure.step('Click save in edit personal details')
    def ed2_save(self):
        return self.find(ed_save).click()