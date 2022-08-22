from django.apps import AppConfig


class Cysecapp7Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cysecapp7'

    def ready(self):
        # Makes sure all signal handlers are connected
        from cysecapp7 import handlers  # noqa
