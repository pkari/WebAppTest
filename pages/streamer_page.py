import logging

from selenium.webdriver.common.by import By
from helpers.web_element_helper import WebElementHelper
from selenium.common.exceptions import NoSuchElementException


class StreamerPage:
    FOLLOW_BUTTON = (By.CSS_SELECTOR, "div[data-a-target='tw-code-button-label-text']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, ".popup-close")  # I have not seen that modal,
    # that the home assignment description talks about

    def __init__(self, driver, timeout):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.weh = WebElementHelper(driver, timeout)

    def is_loaded(self):
        """
        Returns True if the unique element is visible, else False.
        """
        try:
            self.weh.wait_until_visible(self.FOLLOW_BUTTON)
            self.logger.info("Streamer page loaded.")
            return True
        except Exception:
            self.logger.warning("Streamer page failed to load.")
            return False

    def close_optional_modal(self):
        """
        Attempts to close a popup if it appears. Does nothing if popup is not present.
        """
        try:
            close_button = self.driver.find_element(*self.MODAL_CLOSE_BUTTON)
            close_button.click()
            self.logger.info("Modal closed")

        except NoSuchElementException:
            self.logger.info("Modal did not appear.")

    def take_screenshot(self, test_name="", pic_name=""):
        self.weh.take_screenshot(test_name, pic_name)


