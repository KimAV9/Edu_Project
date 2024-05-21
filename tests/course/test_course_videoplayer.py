import allure
import pytest
from pages.course_page import VideoPlayerCheck
from time import sleep
import pytest_order

def test_video_player_check(browser):
    video_player_check = VideoPlayerCheck(browser)

    video_player_check.temp_open()
    #video_player_check.playback_assertion_1()
    #video_player_check.playback_to_text()
    video_player_check.playback_current_assert()
    video_player_check.check_playback()


