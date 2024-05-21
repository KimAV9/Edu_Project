from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
import random
import allure
from time import sleep
import pytest
from bs4 import BeautifulSoup

n_click_notification = (By.XPATH, '')

l_click_language_menu = (By.XPATH, '')
l_choose_language = (By.XPATH, '')
l_choose_language_eng = (By.XPATH, '')
l_check_translation = ()

s_open_filter = (By.XPATH, '')

d_open_filter =(By.XPATH, '')