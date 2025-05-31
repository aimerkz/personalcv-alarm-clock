from contextlib import suppress

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config import settings
from services.interfaces import BaseAlarmService


class AlarmService(BaseAlarmService):
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def wake_up_app(self) -> None:
        self.driver.get(settings.APP_URL)
        self._check_and_click_button()
        self._verify_content_loaded()

    def _check_and_click_button(self) -> None:
        with suppress(TimeoutException):
            if button := WebDriverWait(self.driver, settings.BUTTON_CLICK_TIMEOUT).until(
                ec.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//button[normalize-space()="Yes, get this app back up!"]',
                    ),
                )
            ):
                button.click()

    def _verify_content_loaded(self) -> None:
        with suppress(TimeoutException):
            iframe = WebDriverWait(self.driver, settings.SWITCH_TO_IFRAME_TIMEOUT).until(
                ec.presence_of_element_located(
                    (By.TAG_NAME, "iframe"),
                )
            )
            self.driver.switch_to.frame(iframe)

            WebDriverWait(self.driver, settings.PAGE_LOAD_TIMEOUT).until(
                ec.presence_of_element_located(
                    (By.ID, "artem-merkulov"),
                )
            )
