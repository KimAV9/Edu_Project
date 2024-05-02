import random


class Accout_profile_locators_wokrexp():
    x = random.randint(1, 12)
    y = x - 1
    addworkexp = '//div[@class="cds-9 css-dv86ch cds-10 cds-18 cds-29"]/descendant::button[@class ="cds-149 cds-button-disableElevation cds-button-secondary css-1pddt1l"]'

    nameofinstitution = '//span[@class="fs-mask"]/descendant::button[@class="css-1sifyul"]'
    addnameofinstitution = '//div[@class="menu-item-inactive css-1bol722"]'
    text_inst = '//span[@data-e2e="profile-work-institution"]/descendant::p[text()=""]'

    createitem = '//button[@class ="cds-149 cds-button-disableElevation cds-button-ghost css-htiquy"]'
    deletetext = '//div[@class ="css-vu83vx"]'
    close = '//button[@class="cds-149 cds-button-disableElevation cds-button-ghost css-1s96oj"]'

    role = f'//div[@class="menu-item-inactive css-1bol722"][{random.randint(1, 100)}]'
    addrole = '//div[@data-e2e="profile-work-role"]'
    text_role = '//div[@data-e2e="profile-work-role"]/descendant::p[text()=""]]'

    startmounth = '//div[@data-e2e= "profile-work-start"]/descendant::div[@class = "cds-204 cds-205 cds-select-select cds-208 cds-241 cds-225 cds-input-input"][1]'
    addstartmounth = f'//li[@class ="cds-149 cds-1564 cds-1560 cds-selectOption-root css-xzdz7m cds-1561 cds-1571 cds-1572 cds-selectOption-button"][{random.randint(1, 12)}]'

    startyear = '//div[@data-e2e= "profile-work-start"]/descendant::div[@class = "cds-204 cds-205 cds-select-select cds-208 cds-241 cds-225 cds-input-input"][2]'
    addstartyear = f'//li[@class ="cds-149 cds-1611 cds-1607 cds-selectOption-root css-xzdz7m cds-1609 cds-selectOption-selected cds-1608 cds-1618 cds-1619 cds-selectOption-button cds-1621"][{y}]'

    endmounth = '//div[@data-e2e= "profile-work-end"]/descendant::div[@class = "cds-204 cds-205 cds-select-select cds-208 cds-241 cds-225 cds-input-input"][1]'
    addendmounth = '//li[@class="cds-149 cds-1748 cds-1744 cds-selectOption-root css-xzdz7m cds-1745 cds-1755 cds-1756 cds-selectOption-button"]'

    endyear = '//div[@data-e2e= "profile-work-end"]/descendant::div[@class = "cds-204 cds-205 cds-select-select cds-208 cds-241 cds-225 cds-input-input"][2]'
    addendyear = f'//li[@class="cds-149 cds-1842 cds-1838 cds-selectOption-root css-xzdz7m cds-1839 cds-1849 cds-1850 cds-selectOption-button"][{x}]'

    stillwork = '//label[@class="cds-checkboxAndRadio-label"]'
    stillworklocked = '//div[@class="cds-1899 cds-1900 cds-select-select cds-select-readOnly cds-1903 cds-1936 cds-1920 cds-input-input"]'

    description = '//div[@data-e2e="profile-work-description"]/child::textarea[1]'

    save = '//button[@data-e2e="profile-work-save"]'
    remove = '//button[@data-track-component="profile_remove_work_history"]'


class Accout_profile_locators_education():
    x = random.randint(1, 12)
    y = x - 1

    nameofinst = '//button[@class="css-1sifyul"]'
    addnameofinst = f'//div[@class="menu-item-inactive css-1bol722"][{random.randint(1, 10)}]'

    degree = '//div[@data-e2e= "profile-education-degree"]/descendant::div[@class = "cds-438 cds-439 cds-select-select cds-442 cds-475 cds-459 cds-input-input"]'
    add_degree = f'//li[@class="cds-149 cds-3472 cds-3468 cds-selectOption-root css-xzdz7m cds-3469 cds-3479 cds-3480 cds-selectOption-button"][{random.randint(3, 7)}]'

    discipline = '//div[@data-e2e="profile-education-discipline"]/descendant::div[@class="cds-438 cds-439 cds-select-select cds-442 cds-475 cds-459 cds-input-input"]'
    add_discipline = f'//li[@class="cds-149 cds-4365 cds-4361 cds-selectOption-root css-xzdz7m cds-4362 cds-4372 cds-4373 cds-selectOption-button"][{random.randint(1, 12)}]'
    area_of_conc = '/html/body/div[5]/div[3]/div/div/div[2]/div[2]/div/div/div[4]/div[1]/fieldset'

    startmounth = '//div[@data-e2e= "profile-education-start-date"]/descendant::div[@class = "cds-464 cds-449 cds-input-root cds-input-onLight cds-select-field-root css-nuguie cds-465"][1]'
    addstartmounth = f'//li[@class ="cds-149 cds-4412 cds-4408 cds-selectOption-root css-xzdz7m cds-4409 cds-4419 cds-4420 cds-selectOption-button"][{random.randint(1, 12)}]'

    startyear = '//div[@data-e2e= "profile-education-start-date"]/descendant::div[@class = "cds-464 cds-449 cds-input-root cds-input-onLight cds-select-field-root css-nuguie cds-465"][2]'
    addstartyear = f'//li[@class ="cds-149 cds-4553 cds-4549 cds-selectOption-root css-xzdz7m cds-4550 cds-4560 cds-4561 cds-selectOption-button"][{y}]'

    endmounth = '//div[@data-e2e= "profile-education-end-date"]/descendant::div[@class = "cds-464 cds-449 cds-input-root cds-input-onLight cds-select-field-root css-nuguie cds-465"][1]'
    addendmounth = '//li[@class="cds-149 cds-4506 cds-4502 cds-selectOption-root css-xzdz7m cds-4504 cds-selectOption-selected cds-4503 cds-4513 cds-4514 cds-selectOption-button cds-4516"]'

    endyear = '//div[@data-e2e= "profile-education-end-date"]/descendant::div[@class = "cds-464 cds-449 cds-input-root cds-input-onLight cds-select-field-root css-nuguie cds-465"][2]'
    addendyear = f'//li[@class="cds-149 cds-4600 cds-4596 cds-selectOption-root css-xzdz7m cds-4597 cds-4607 cds-4608 cds-selectOption-button"][{x}]'

    grade = "/html/body/div[5]/div[3]/div/div/div[2]/div[2]/div/div/div[8]/div/fieldset"

    save = '//button[@data-track-component="profile_save_education_history"]'


class AddInfo():
    add = '//section[@class="css-1gqjnbp"]/descendant::button[@data-track-component="profile_add_work_preferences"]'
    about = '//div[@class="cds-687 cds-672 cds-input-root cds-text-field-root cds-input-onLight css-pphb6b cds-697 cds-688 cds-695 cds-680 cds-input-multiline"]/child::textarea[1]'
    save = '//button[@data-track-component="profile_additional_info_save"]'


class WorkPref():
    dropdown_menu = '/*[name()="svg" and @data-testid = "icon-not-active"]'  #still udner work

    delete_role = '//button[@data-testid="delete-role-preference-button"]'
    create_item = '//button[@class ="cds-149 cds-button-disableElevation cds-button-ghost css-1dab2db"]'

    add_role = '//div[@data-e2e="profile_edit_role"]/descendant::*[@class="css-1sifyul"][1]'
    add_industry = '//div[@data-e2e="profile_edit_role"]/descendant::*[@class="css-1sifyul"][2]'
    add_another_role = '//button[@data-track-component="profile_add_work_preferences_role"]'

    add_role2 = ''  #underconstruction
    add_industry2 = ''


class ProfileVisibility():
    share_link = '//section[@data-e2e="profile-photo-and-invitation-section"]/descendant::button[3]'
    copy_link = '//div[@data-track-component="profile_share_public_profile_dialog"]/descendant::button[1]'

    customize_link = '//div[@data-track-component="profile_share_public_profile_dialog"]/descendant::button[2]'
    enter_customization = '//input[@aria-label="Profile Link"]'
    save_custom = '//button[@class="cds-149 cds-button-disableElevation cds-button-primary css-ra3hwj"]'
    cancel_custom = '//div[@class="css-1hllf5q"]/descendant::button[@class="cds-149 cds-button-disableElevation cds-button-ghost css-l0otf2"][1]'
    got_it_btn = '//button[@data-e2e="share-profile-got-it"]'

    update_visibility = '//section[@data-e2e="profile-photo-and-invitation-section"]/descendant::button[4]'
    anyone_with_link = '//label[@class="cds-checkboxAndRadio-label"]'
    done = '//button[@class="cds-149 cds-button-disableElevation cds-button-primary css-ra3hwj"]'


class EditIntroProf():
    edit_btn = '//button[@data-e2e="profile_edit_intro_profile"]'
    edit_name = '//input[@name="fullName"]'
    edit_pronoun = '//input[@name="pronoun"]'

    edit_gender = '//div[@class="cds-1038 cds-1039 cds-select-select cds-1042 cds-1027 cds-1011 cds-input-input"]'
    choose_gender = f'//ul[@class="cds-1175 cds-1050 cds-select-list cds-1176"]/child::li[{random.randint(1, 8)}]'
    save = '//button[@data-track-component="profile_save_intro_profile"]'