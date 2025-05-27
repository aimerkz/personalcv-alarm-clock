import sys
import logging
import tempfile
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


def _set_options() -> Options:
    options = Options()

    options.add_argument("--headless")
    options.add_argument("--mute-audio")
    options.add_argument("--enable-javascript")
    options.add_argument("--disable-dev-shm-usage")

    user_data_dir = os.path.join(tempfile.gettempdir(), "chrome_profile")
    os.makedirs(user_data_dir, exist_ok=True)
    options.add_argument(f"--user-data-dir={user_data_dir}")

    return options


def main() -> None:
    service = webdriver.ChromeService(log_output=sys.stdout, port=0)
    options = _set_options()

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://amerkulovcv.streamlit.app")

    try:
        button = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable(
                (By.XPATH, '//button[normalize-space()="Yes, get this app back up!"]'),
            )
        )
        button.click()

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.ID, "artem-merkulov"),
            )
        )
    except TimeoutException:
        logger.error("Timed out waiting for page to load")
    finally:
        logger.info("Success, by!")
        driver.quit()


if __name__ == "__main__":
    main()
