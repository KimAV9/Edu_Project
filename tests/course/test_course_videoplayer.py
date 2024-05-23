import allure
import pytest
from pages.course_page import VideoPlayerCheck
from time import sleep
import pytest_order

@pytest.mark.order(18)
def test_video_player_check(browser):
    video_player_check = VideoPlayerCheck(browser)

    video_player_check.temp_open()
    sleep(3)
    video_player_check.click_pause()
    video_player_check.click_mute()
    video_player_check.click_autoplay()

    video_player_check.click_subs()
    video_player_check.turn_off_subs()
    video_player_check.turn_on_subs1()
    video_player_check.check_subs()

    video_player_check.click_settings()
    video_player_check.playback_assertion_1()
    video_player_check.playback_assertion_2()
    video_player_check.playback_to_click_check()

    video_player_check.quality_assertion_1()
    video_player_check.quality_assertion_2()
    video_player_check.quality_to_assert()
    browser.quit()



