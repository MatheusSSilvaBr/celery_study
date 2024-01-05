QUEUE_NAME ?= "celery"
MESSAGE_QUEUE ?= file://message-event.json
MESSAGE_ATTRIBUTES ?= file://message-attributes.json

create-queue:
	@aws sqs create-queue --queue-name $(QUEUE_NAME) --endpoint-url http://localhost:4566 --region us-east-1

list-queues:
	aws sqs list-queues --endpoint-url http://localhost:4566 --region us-east-1

receive-message:
	@aws sqs receive-message --queue-url http://localhost:4566/000000000000/$(QUEUE_NAME) --endpoint-url http://localhost:4566 --region us-east-1

send-message:
	@aws sqs send-message --queue-url http://localhost:4566/000000000000/$(QUEUE_NAME) --message-body $(MESSAGE_QUEUE) --endpoint-url http://localhost:4566 --region us-east-1



prod-send-message:
	aws sqs send-message --queue-url 	https://sqs.us-east-1.amazonaws.com/338505395337/celery --message-body $(MESSAGE_QUEUE) --region us-east-1 --profile localstack --message-attributes $(MESSAGE_ATTRIBUTES)