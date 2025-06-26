# create a function to consume messages from a Kafka topic
from kafka import KafkaConsumer

def consume_kafka_messages(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
    for message in consumer:
        print(f"Received message: {message.value.decode('utf-8')}")

consume_kafka_messages('topic1')