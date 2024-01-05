broker_url = "sqs://localhost:4566"

broker_transport_options= {
            'predefined_queues':{
                'celery': {
                    'url': 'http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/celery',
                }  
            }
}            
task_serializer='json'
result_serializer='json'
accept_content=['json']
timezone='America/Sao_Paulo'
enable_utc=True
result_backend = None
eneble_remote_control = False