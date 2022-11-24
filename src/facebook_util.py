import constants
import facebook_credentials

from selenium import webdriver
from selenium.webdriver.common.by import By


def login_to_facebook(driver: webdriver.Chrome) -> None:
    """
    Selenium opens Chrome in a private window each time, so no passwords or sessions are saved. This means we
    need to login to Facebook each time we run these scripts.

    This function logs the browser into Facebook so we can access Candy Crush.

    :param driver:  Chrome Webdriver that automates interactions with Chrome.
    :return:        None.
    """
    username_entry = driver.find_element(By.XPATH, constants.EMAIL_ENTRY_XPATH)
    username_entry.send_keys(facebook_credentials.USERNAME)

    password_entry = driver.find_element(By.XPATH, constants.PASSWORD_ENTRY_XPATH)
    password_entry.send_keys(facebook_credentials.PASSWORD)

    driver.find_element(By.XPATH, constants.LOGIN_BUTTON_XPATH).click()
