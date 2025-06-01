from dishka import Provider, Scope, from_context

from config.settings import Settings


class SettingsProvider(Provider):
    settings = from_context(provides=Settings, scope=Scope.APP)
