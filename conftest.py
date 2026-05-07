import pytest
import os
from selenium import webdriver

os.environ["SE_AVOID_STATS"] = "true"


@pytest.fixture
def driver():

    run_mode = os.getenv("RUN_MODE", "local")  # default = local

    if run_mode == "local":
        driver = webdriver.Chrome()

    elif run_mode == "grid":
        options = webdriver.ChromeOptions()

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )

    else:
        raise ValueError("Invalid RUN_MODE. Use 'local' or 'grid'")

    driver.maximize_window()

    yield driver

    driver.quit()