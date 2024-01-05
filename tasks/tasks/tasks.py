from celery_app.utils import get_celery_app

celery = get_celery_app()

@celery.task(name="tasks", bind=True, max_retries=3, queue="celery")
def ola_mundo(self, **kwargs):
    print(f"Task job (celery): {kwargs}")

