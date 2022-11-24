import constants

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_chrome_webdriver() -> webdriver.Chrome:
    """
    Builds and returns the Chrome webdriver that we will use to automate interactions with Chrome.

    :return:    Chrome Webdriver that automates interactions with Chrome.
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    return webdriver.Chrome(service=Service(constants.SELENIUM_EXECUTABLE_PATH), options=chrome_options)
