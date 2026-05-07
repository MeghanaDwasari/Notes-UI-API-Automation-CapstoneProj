from pages.login_page import LoginPage
from pages.home_page import HomePage
from config.environment import get_config
from selenium.webdriver.support.ui import WebDriverWait
from utils.logger import get_logger

logger = get_logger()


def test_login(driver):

    logger.info("Starting Login Test")

    config = get_config()

    driver.get(config["base_url"])

    logger.info("Application URL opened")

    WebDriverWait(driver, 30).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    logger.info("Page fully loaded")

    login = LoginPage(driver)

    login.login(config["email"], config["password"])

    logger.info("Login completed")

    home = HomePage(driver)

    assert home.is_home_loaded()

    logger.info("Home page loaded successfully")