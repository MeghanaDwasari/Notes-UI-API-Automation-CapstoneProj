import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from api.api_client import APIClient
from api.notes_api import NotesAPI
from config.environment import get_config


def test_notes_api_performance():
    config = get_config()
    client = APIClient(config["api_url"])
    client.login(config["email"], config["password"])
    api = NotesAPI(client)

    res, elapsed = api.get_notes()

    assert res.status_code == 200
    notes_count = len(res.json().get("data", []))
    threshold = 1.5 + (notes_count * 0.05)

    assert elapsed < threshold, (
        f"Notes API too slow: {elapsed:.2f}s (limit: {threshold:.2f}s, notes: {notes_count})"
    )


def test_ui_login_performance(driver):
    config = get_config()

    
    driver.get(config["base_url"])

    login = LoginPage(driver)

    
    start = time.time()

    login.login(config["email"], config["password"])

    
    WebDriverWait(driver, 10).until(
        EC.url_contains("notes")
    )

    elapsed = time.time() - start

    # Step 4: Assertion with realistic threshold
    assert elapsed < float(config.get("ui_login_threshold", 20.0)), (
        f"UI login flow is too slow: {elapsed:.2f}s"
    )