# Kafka Commands

## Commands ran in command prompt

### Run Zookeeper
> .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

### Run Kafka Broker
> .\bin\windows\kafka-server-start.bat .\config\server.properties

### Create Topic
> .\bin\windows\kafka-topics.bat --create --topic topic1 --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3


