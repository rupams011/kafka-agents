# create a kafka producer function that sends messages to a topic
from kafka import KafkaProducer

def send_kafka_message(topic, message):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send(topic, message.encode('utf-8'))
    producer.close()



# send a kafka message to a topic every 5 secondsimport time
import time
def produce_kafka_messages(topic):
    while True:
        message = f"Hello, Kafka! {time.time()}"
        send_kafka_message(topic, message)
        print(f"Sent message: {message}")
        time.sleep(5)

produce_kafka_messages('topic1')
