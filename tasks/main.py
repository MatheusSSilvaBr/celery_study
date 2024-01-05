from fastapi import FastAPI
from celery_app.utils import get_celery_app
from tasks.tasks import ola_mundo

app = FastAPI()
app.celery_app = get_celery_app()

celery = app.celery_app

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ola_mundo/{query}")
def queue_task(query):
    kwargs = {"query": query}
    ola_mundo.apply_async(queue="celery", kwargs=kwargs)


