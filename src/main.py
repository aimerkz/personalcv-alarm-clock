from dishka import make_container

from config.settings import Settings
from core.providers.alarm import AlarmProvider
from core.providers.webdriver import WebDriverProvider
from services.interfaces import BaseAlarmService


def main() -> None:
    container = make_container(
        WebDriverProvider(),
        AlarmProvider(),
        context={Settings: Settings()},
    )
    with container() as c:
        service = c.get(BaseAlarmService)
        service.wake_up_app()


if __name__ == "__main__":
    main()
