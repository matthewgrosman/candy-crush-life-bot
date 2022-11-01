# main.py
import constants
import facebook_credentials
import iframe_util

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver: webdriver.Chrome) -> None:
    """
    Selenium opens Chrome in a private window each time, so no passwords or sessions are saved. This means we
    need to login to Facebook each time we run these scripts.

    This function logs the browser into Facebook so we can access Candy Crush.

    :param driver:  Chrome webdriver that automates interactions with Chrome.
    :return:        None.
    """
    username_entry = driver.find_element(By.XPATH, constants.EMAIL_ENTRY_XPATH)
    username_entry.send_keys(facebook_credentials.USERNAME)

    password_entry = driver.find_element(By.XPATH, constants.PASSWORD_ENTRY_XPATH)
    password_entry.send_keys(facebook_credentials.PASSWORD)

    driver.find_element(By.XPATH, constants.LOGIN_BUTTON_XPATH).click()


def find_game_iframe(driver: webdriver.Chrome) -> WebElement:
    """
    The game is not rendered directly in the source HTML, but rather is inside an iFrame.

    This function finds the iFrame holding the game, waits until it is present on-screen, and then returns that
    iFrame as an element we can interact with.

    :param driver:  Chrome webdriver that automates interactions with Chrome.
    :return:        A WebElement that represents the iFrame the game is held in.
    """
    return WebDriverWait(driver, constants.SELENIUM_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, constants.IFRAME_XPATH))
    )


def send_lives(driver: webdriver.Chrome, iframe: WebElement) -> None:
    pass
    # Click on life button
    iframe_util.click_life_button(driver, iframe)

    # Click "Send" button
    iframe_util.click_send_button(driver, iframe)

    # De-select all friends
    iframe_util.click_select_all_friends_button(driver, iframe)

    # Select friends
    iframe_util.click_friend_button(driver, iframe)

    # Click "Send" button
    iframe_util.click_send_button(driver, iframe)


if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(constants.SELENIUM_EXECUTABLE_PATH))
    driver.get(constants.CANDY_CRUSH_URL)

    login(driver)

    canvas_xpath = '//*[@id="canvas"]'

    iframe = find_game_iframe(driver)
    send_lives(driver, iframe)

    # ActionChains(driver=driver).move_to_element(canvas).click().perform()
