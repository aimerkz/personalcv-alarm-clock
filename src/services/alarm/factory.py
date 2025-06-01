from selenium import webdriver

from config import settings
from services.alarm.service import AlarmService
from services.interfaces import BaseAlarmService, BaseAlarmServiceFactory


class AlarmServiceFactory(BaseAlarmServiceFactory):
    def create(
        self, driver: webdriver.Chrome, config: settings.Settings
    ) -> BaseAlarmService:
        return AlarmService(driver, config)
