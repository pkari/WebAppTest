import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from helpers.web_element_helper import WebElementHelper
from pages.streamer_page import StreamerPage


class TwitchPage:
    URL = "https://www.twitch.com"

    KEEP_USING_WEB_BUTTON = (By.XPATH, "//button[contains(., 'Keep using web')]")
    CONSENT_ACCEPT_BUTTON = (By.CSS_SELECTOR, "button[data-a-target='consent-banner-accept']")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "div[data-a-target='tw-core-button-label-text']")
    SEARCH_ICON = (By.XPATH, "//*[@id='root']/div[2]/a[2]/div/div[1]")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[data-a-target='tw-input']")
    STREAMER_CARD = (By.XPATH, "//*[@id='page-main-content-wrapper']/div/div/div[1]/div/div/div[3]")
    VIEW_ALL_CHANNELS = (By.CSS_SELECTOR, "p[aria-label='View All Channel Search Results']")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.logger = logging.getLogger(__name__)
        self.weh = WebElementHelper(driver, timeout)

    def handle_keep_using_web_popup(self, retries=5, delay=1):
        for attempt in range(retries):
            try:
                self.weh.click(self.KEEP_USING_WEB_BUTTON)
                self.logger.info("Closing popup")
                return  # Success, exit the method
            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
                if attempt < retries - 1:
                    time.sleep(delay)
                else:
                    self.logger.info("Popup did not appear after retries, continue silently")
                    pass

    def accept_cookies(self, retries=5, delay=1):
        for attempt in range(retries):
            try:
                self.weh.click(self.CONSENT_ACCEPT_BUTTON)
                self.logger.info("Accepting cookies")
                return
            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
                if attempt < retries - 1:
                    self.logger.info(f"Attempt {attempt + 1} failed with exception: {e}")
                    time.sleep(delay)
                else:
                    self.logger.info("Cookie panel did not appear after retries, continue silently")
                    pass

    def load(self):
        self.logger.info(f"Loading {self.URL}")
        self.driver.get(self.URL)

    def is_loaded(self):
        try:
            self.weh.wait_until_visible(self.SIGN_UP_BUTTON)
            self.logger.info(f"Twitch page loaded")
            return True
        except Exception:
            self.logger.info(f"Twitch page has not been loaded")
            return False

    def click_search_icon(self):
        self.weh.click(self.SEARCH_ICON)

    def click_search_input(self):
        self.weh.click(self.SEARCH_INPUT)

    def enter_search_query(self, query):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(query)
        self.logger.info(f"Search with {query}")
        search_input.send_keys(Keys.ENTER)

    def select_all_channels(self):
        self.logger.info(f"Selecting all channels")
        self.weh.click(self.VIEW_ALL_CHANNELS)

    def scroll_down(self, scroll_number=1, pixels=500):
        self.weh.scroll_down(scroll_number, pixels)

    def open_streamer_page(self):
        """
        Clicks on the third streamer card/link to open the streamer page.
        """
        self.weh.click(self.STREAMER_CARD)
        self.logger.info(f"Open Streamer page")
        return StreamerPage(self.driver, self.timeout)
