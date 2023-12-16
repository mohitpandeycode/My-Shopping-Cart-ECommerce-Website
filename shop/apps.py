from django.apps import AppConfig


class ShopConfig(AppConfig):  # we can use this cofig in the place of mac -> settings.py -> installed apps-> 'shop' to 'shop.apps.ShopConfig'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
