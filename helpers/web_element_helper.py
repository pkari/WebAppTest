import time
import logging

from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebElementHelper:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        """
        Waits until the element located by 'locator' is clickable, then clicks it.
        """
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def take_screenshot(self, test_name="noname", pic_name="noname", extension="png"):
        screenshot_dir = "screenshots"
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # e.g., 2024-06-12_15-30-45
        screenshot_name = f"{test_name}-{pic_name}-{timestamp}.{extension}"
        self.logger.info(f"Screenshot is taken with name: {screenshot_name}")
        self.driver.save_screenshot(f"{screenshot_dir}/{screenshot_name}")

    def wait_until_visible(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def scroll_down(self, scroll_number=1, pixels=500):
        self.logger.info(f"Scrolling the page")
        for _ in range(scroll_number):
            self.driver.execute_script(f"window.scrollBy(0, {pixels});")
            time.sleep(1)
