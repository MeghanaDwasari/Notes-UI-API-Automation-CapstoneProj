
from tenacity import retry, stop_after_attempt, wait_fixed
from selenium.common.exceptions import WebDriverException

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def safe_get(driver, url):
    driver.get(url)
