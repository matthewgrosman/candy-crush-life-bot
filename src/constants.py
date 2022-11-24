# Path to the selenium executable file on my computer.
SELENIUM_EXECUTABLE_PATH = "/Users/matthew/Documents/Programming/selenium-driver/chromedriver"

# The URL to the Candy Crush game. We feed this to the Chrome Webdriver.
CANDY_CRUSH_URL = "https://apps.facebook.com/candycrushsoda"

# The time we wait for an HTML element to become present on the webpage.
SELENIUM_TIMEOUT = 600

# The amount of seconds we wait for the game to load before we begin sending lives.
GAME_LOAD_TIME = 25

# XPATH constants
EMAIL_ENTRY_XPATH = '//*[@id="email"]'
PASSWORD_ENTRY_XPATH = '//*[@id="pass"]'
LOGIN_BUTTON_XPATH = '//*[@id="loginbutton"]'
IFRAME_XPATH = '//*[@id="iframe_canvas"]'

# The time to wait between each button click. This allows time for resources to load in.
TIME_TO_SLEEP = 3
