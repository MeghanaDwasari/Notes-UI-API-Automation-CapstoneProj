from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.environment import get_config
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_empty_note_validation(driver):
    config = get_config()

    driver.get(config["base_url"])

    login = LoginPage(driver)
    login.login(config["email"], config["password"])

    notes = ProductPage(driver)

    
    WebDriverWait(driver, 10).until(
        lambda d: len(notes.get_all_notes()) >= 0
    )

    before_count = len(notes.get_all_notes())

    notes.click(notes.ADD_NOTE)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(notes.TITLE)
    )

    notes.click(notes.SAVE)

    title_error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'invalid-feedback') and normalize-space(text())='Title is required']")
        )
    )

    desc_error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'invalid-feedback') and normalize-space(text())='Description is required']")
        )
    )

    assert title_error.is_displayed()
    assert desc_error.is_displayed()

    
    WebDriverWait(driver, 10).until(
        lambda d: len(notes.get_all_notes()) >= before_count
    )

    after_count = len(notes.get_all_notes())

    assert after_count == before_count