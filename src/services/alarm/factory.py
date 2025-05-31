from selenium.webdriver import Chrome

from services.alarm.service import AlarmService
from services.interfaces import BaseAlarmService, BaseAlarmServiceFactory


class AlarmServiceFactory(BaseAlarmServiceFactory):
    def create(self, driver: Chrome) -> BaseAlarmService:
        return AlarmService(driver)
