from abc import ABC, abstractmethod

from selenium import webdriver

from config.settings import Settings


class BaseAlarmService(ABC):
    @abstractmethod
    def wake_up_app(self) -> None:
        pass


class BaseAlarmServiceFactory(ABC):
    @abstractmethod
    def create(self, driver: webdriver.Chrome, config: Settings) -> BaseAlarmService:
        pass
