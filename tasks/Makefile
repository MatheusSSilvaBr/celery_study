start-app:
	@uvicorn main:app --reload

start-worker:
	@celery -A main.celery worker --loglevel=INFO
