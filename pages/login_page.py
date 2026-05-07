from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, "//button[text()='Login']")

    def login(self, email, password):
        wait = WebDriverWait(self.driver, 15)

        # ALWAYS use stable URL
        self.driver.get(self.base_url + "/login")

        wait.until(EC.visibility_of_element_located(self.EMAIL))

        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)

        self.click(self.LOGIN_BTN)

        wait.until(EC.url_contains("notes"))
