default_app_config='polls.apps.MyappConfig'
from .celery import app as celery_app

__all__ = ['celery_app']