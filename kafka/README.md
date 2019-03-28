
pip install kafka-python

zookeeper
docker create --name zookeeper --network host wurstmeister/zookeeper
kafka
docker create --name kafka \
--network host \
-e KAFKA_BROKER_ID=0 \
-e KAFKA_ZOOKEEPER_CONNECT=127.0.0.1:2181 \
-e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://127.0.0.1:9092 \
-e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 wurstmeister/kafka


#创建topic
kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 3 --partitions 1 --topic my-replicated-topic

#查询所有topic
kafka-topics.sh --list --zookeeper localhost:2181
#describe topic
kafka-topics.sh --describe --zookeeper localhost:2181 --topic my-replicated-topic

#发送消息
kafka-console-producer.sh --broker-list localhost:9092 --topic test

#消费消息
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic foobar --from-beginning
