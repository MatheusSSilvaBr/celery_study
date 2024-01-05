from tasks import ola_mundo

ola_mundo.delay()

#  celery -A tasks worker --loglevel=INFO 
#  celery -A tasks flower
