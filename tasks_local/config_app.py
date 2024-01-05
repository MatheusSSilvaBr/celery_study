from celery import Celery




def get_celery_app():

    app = Celery()
    app.config_from_object('celeryconfig')

    return app