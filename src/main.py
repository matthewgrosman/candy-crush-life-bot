import time
import constants

import facebook_util
import iframe_util
import webdriver_util


def start_sending_lives() -> None:
    """
    Entry function for program. This function calls all necessary functions to automatically
    send lives in Candy Crush.

    :return: None.
    """
    driver = webdriver_util.get_chrome_webdriver()
    driver.get(constants.CANDY_CRUSH_URL)

    facebook_util.login_to_facebook(driver)

    # Wait for game to load.
    time.sleep(constants.GAME_LOAD_TIME)

    iframe = iframe_util.find_game_iframe(driver)
    iframe_util.send_lives(driver, iframe)


if __name__ == '__main__':
    start_sending_lives()
