from django.apps import AppConfig


class ContactsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mobile.contacts'
    label = 'mobile_contacts'
    verbose_name = 'Mobile Contacts'