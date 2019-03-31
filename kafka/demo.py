'''
pip install pykafka

'''

from pykafka import KafkaClient

client = KafkaClient(hosts="127.0.0.1:9092")
topic = client.topics['PYKAFKA.TOPIC.TEST']

#product
with topic.get_sync_producer() as producer:
    for i in range(4):
        producer.produce(b'this is a test message')

#consumer
consumer = topic.get_simple_consumer()
for message in consumer:
    if message is not None:
        print(message.offset, message.value)

        
                