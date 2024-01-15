from kombu.utils.url import safequote
from kombu import Queue

aws_access_key = safequote("exemplo")
aws_secret_key = safequote("exemplo")


broker_url = "sqs://{aws_access_key}:{aws_secret_key}@".format(
    aws_access_key=aws_access_key, aws_secret_key=aws_secret_key,
)

broker_transport = "sqs"
broker_transport_options = {
    "region": "us-east-1",
}
task_default_queue = 'default'
task_queues = (
  Queue("celery"),
  Queue("default"),
  )
result_backend = None
accept_content = ["json", "pickle"]
task_serializer = "pickle"
result_serializer = "pickle"
worker_prefetch_multiplier = 1
broker_connection_retry_on_startup = True

worker_concurrency = 1

include: list =('tasks')
