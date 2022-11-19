
from kafka import KafkaConsumer
from json import loads
import json
consumer=KafkaConsumer('consumer',bootstrap_servers=['localhost:9092'],api_version=(0,10))
a=[]
for i in consumer:
    print(i.value)
 

# with open('solution-task1.txt', 'w') as f:
    
#     f.writelines("%s\n" % length for length in a)


