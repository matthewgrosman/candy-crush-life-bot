import constants
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def _get_button_list() -> list[dict]:
    """
    There are 4 buttons we must click in order to send a life in Candy Crush.

    1) The first button is a heart-shaped button, this brings up the menu that allows us to send lives.
    2) The next button is a button labeled "Send lives". This brings up a menu of people who we can send lives to.
    3) The next button is technically optional. We are currently on a menu of people who we can send lives to.
    Candy Crush automatically selects all friends when we enter this menu. Since I only have 2 friends on Candy
    Crush (lol), I simply uncheck the one friend who I don't want to send lives to via clicking the button that has
    their name on it.
    4) The final button is a button labeled "Send". This button sends a life to the selected friend.

    We must click the buttons in the order stated above. This function returns a list of coordinates for each
    aforementioned button, and the list is in the correct order as specified above. Each coordinate is a
    dictionary which holds an X coordinate and a Y coordinate.

    :return: A list of button coordinates that contains all of the buttons we need to click to send a life. The list
    is in the correct order we need to click each button in. Each coordinate is a dictionary which holds an X
    coordinate and a Y coordinate.
    """
    # TO-DO: Change this to a proportional coordinate system instead of a pixel-based coordinate system so
    # this will work on any size display.
    heart_button = {'x': -165, 'y': -250}
    send_lives_button = {'x': 0, 'y': 150}
    uncheck_button = {'x': 0, 'y': -50}
    final_send_button = {'x': 0, 'y': 250}

    return [heart_button, send_lives_button, uncheck_button, final_send_button]


def _click_buttons(driver: webdriver.Chrome, iframe: WebElement, button_list: list[dict]) -> None:
    """
    This function takes the list of buttons we need to click in order to send a life and clicks each button
    in the correct order. This is done by using the ActionChains class, where we move the mouse to the appropriate
    coordinate and then perform a mouse click.

    We also add in some buffer time between each click to ensure that each button we want to click on has had
    sufficient time to load into the page. We cannot take advantage of tools such as WebdriverWait since the
    game is contained in an iFrame, and we cannot locate individual buttons as HTML elements- rendering WebdriverWait
    useless. The best approach here is to simply wait for a few seconds to ensure sufficient time for loading.

    :param driver:      Chrome Webdriver that automates interactions with Chrome.
    :param iframe:      iFrame that the Candy Crush game is contained in.
    :param button_list: A list of button coordinates that contains all of the buttons we need to click to send a life.
                        The list is in the correct order we need to click each button in. Each coordinate is a
                        dictionary which holds an X coordinate and a Y coordinate.
    :return:            None.
    """
    actions = ActionChains(driver)

    for button in button_list:
        time.sleep(constants.TIME_TO_SLEEP)
        actions.move_to_element_with_offset(iframe, button['x'], button['y']).click().perform()


def send_lives(driver: webdriver.Chrome, iframe: WebElement) -> None:
    """
    This function is the entry point to sending a life.

    :param driver:  Chrome Webdriver that automates interactions with Chrome.
    :param iframe:  iFrame that the Candy Crush game is contained in.
    :return:        None.
    """
    # It looks like this should be a function call instead, but the line below does perform a scroll.
    iframe.location_once_scrolled_into_view
    button_list = _get_button_list()

    life_counter = 0
    while True:
        _click_buttons(driver, iframe, button_list)
        life_counter += 1
        print(life_counter)


def find_game_iframe(driver: webdriver.Chrome) -> WebElement:
    """
    The game is not rendered directly in the source HTML, but rather is inside an iFrame.

    This function finds the iFrame holding the game, waits until it is present on-screen, and then returns that
    iFrame as an element we can interact with.

    :param driver:  Chrome Webdriver that automates interactions with Chrome.
    :return:        A WebElement that represents the iFrame the game is held in.
    """
    return WebDriverWait(driver, constants.SELENIUM_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, constants.IFRAME_XPATH))
    )
