from pykafka import KafkaClient
import time 
 
class KafkaTest(object):
    """
    测试kafka常用api
    """
    def __init__(self, host="localhost:9092"):
        self.host = host
        self.client = KafkaClient(hosts=self.host)
 
    def producer_partition(self, topic):
        """
        生产者分区查看，主要查看生产消息时offset的变化
        :return:
        """
        topic = self.client.topics[topic.encode()]
        partitions = topic.partitions
        print (u"查看所有分区 {}".format(partitions))
 
        earliest_offset = topic.earliest_available_offsets()
        print(u"获取最早可用的offset {}".format(earliest_offset))
 
        # 生产消息之前看看offset
        last_offset = topic.latest_available_offsets()
        print(u"最近可用offset {}".format(last_offset))
 
        # 同步生产消息
        p = topic.get_producer(sync=True)
        p.produce(str(time.time()).encode())
 
        # 查看offset的变化
        last_offset = topic.latest_available_offsets()
        print(u"最近可用offset {}".format(last_offset))
 
    def producer_designated_partition(self, topic):
        """
        往指定分区写消息，如果要控制打印到某个分区，
        需要在获取生产者的时候指定选区函数，
        并且在生产消息的时候额外指定一个key
        :return:
        """
 
        def assign_patition(pid, key):
            """
            指定特定分区, 这里测试写入第一个分区(id=0)
            :param pid: 为分区列表
            :param key:
            :return:
            """
            print("为消息分配partition {} {}".format(pid, key))
            return pid[0]
 
        topic = self.client.topics[topic.encode()]
        p = topic.get_producer(sync=True, partitioner=assign_patition)
        p.produce(str(time.time()).encode(), partition_key=b"partition_key_0")
 
    def async_produce_message(self, topic):
        """
        异步生产消息，消息会被推到一个队列里面，
        另外一个线程会在队列中消息大小满足一个阈值（min_queued_messages）
        或到达一段时间（linger_ms）后统一发送,默认5s
        :return:
        """
        topic = self.client.topics[topic.encode()]
        last_offset = topic.latest_available_offsets()
        print("最近的偏移量 offset {}".format(last_offset))

 
if __name__ == '__main__':
    host = '127.0.0.1:9092'
    kafka_ins = KafkaTest(host)
    topic = 'PYKAFKA.TOPIC.TEST.DEMO'
    kafka_ins.producer_partition(topic)
    # kafka_ins.producer_designated_partition(topic)
    # kafka_ins.async_produce_message(topic)
    #kafka_ins.get_produce_message_report(topic)
