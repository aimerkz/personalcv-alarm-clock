import sys
import tempfile
from typing import Iterable

from dishka import Provider, Scope, provide
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebDriverProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_options(self) -> Options:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--mute-audio")
        options.add_argument("--enable-javascript")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
        return options

    @provide(scope=Scope.REQUEST)
    def get_service(self) -> webdriver.ChromeService:
        return webdriver.ChromeService(log_output=sys.stdout, port=0)

    @provide(scope=Scope.REQUEST)
    def get_driver(
        self, service: webdriver.ChromeService, options: Options
    ) -> Iterable[webdriver.Chrome]:
        driver = webdriver.Chrome(service=service, options=options)
        yield driver
        driver.close()
