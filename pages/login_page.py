from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# 👇 add retry utility
from utils.safe_actions import safe_get


class LoginPage(BasePage):

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, "//button[text()='Login']")

    def login(self, email, password):
        wait = WebDriverWait(self.driver, 20)

        # ✅ FIX 1: safe navigation (handles Grid timeout issues)
        safe_get(self.driver, self.base_url + "/login")

        # ✅ FIX 2: wait for page stability (not just visibility)
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        wait.until(EC.visibility_of_element_located(self.EMAIL))

        # actions
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)

        self.click(self.LOGIN_BTN)

        # ✅ FIX 3: stronger assertion (prevents false pass/fail)
        wait.until(EC.url_contains("notes"))
