from selenium.webdriver.support.ui import WebDriverWait
from config.environment import get_config
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_delete_note_ui(driver):
    config = get_config()

    driver.get(config["base_url"])

    login = LoginPage(driver)
    login.login(config["email"], config["password"])

    notes = ProductPage(driver)

    
    if len(notes.get_all_notes()) == 0:
        notes.create_note("Test Note", "Test Description")

    initial_count = len(notes.get_all_notes())
    assert initial_count > 0

   
    notes.delete_first_note()

   
    WebDriverWait(driver, 20).until(
        lambda d: len(notes.get_all_notes()) == initial_count - 1
    )

    assert len(notes.get_all_notes()) == initial_count - 1