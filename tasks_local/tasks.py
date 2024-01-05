from config_app import get_celery_app

app = get_celery_app()


@app.task
def ola_mundo():
    return 'Olá mundo'

