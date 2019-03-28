import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')

# msg_dict = {
#     "sleep_time": 10,
#     "db_config": {
#         "database": "test_1",
#         "host": "xxxx",
#         "user": "root",
#         "password": "root"
#     },
#     "table": "msg",
#     "msg": "Hello World"
# }
# msg = json.dumps(msg_dict)
# producer.send('test_rhj', msg, partition=0)
# producer.close()


for _ in range(100):
    producer.send('foobar',b'some_messages_bytes')