from dishka import Provider, Scope, provide
from selenium import webdriver

from services.alarm.factory import AlarmServiceFactory
from services.interfaces import BaseAlarmService, BaseAlarmServiceFactory


class AlarmProvider(Provider):
    @provide(scope=Scope.APP)
    def get_alarm_factory(self) -> BaseAlarmServiceFactory:
        return AlarmServiceFactory()

    @provide(scope=Scope.REQUEST)
    def get_alarm_service(
        self,
        driver: webdriver.Chrome,
        factory: BaseAlarmServiceFactory,
    ) -> BaseAlarmService:
        return factory.create(driver)
