'''
from kafka import KafkaProducer
from time import sleep
import json
from datetime import datetime

producer=KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10,1))

producer.send('youtube',b'1')

# a=format(1,'b')
# producer.send('msg',a)

# print(producer)



now=datetime.now()
# datetime.datetime()

current_time=now.strftime("%d/%m%Y %H:%M:%S")

print(current_time)



for i in range(10):
    message='Messages {}'.format(str(datetime.now().time()))
    producer.send('youtube',json.dumps(message).encode('utf-8'))
    sleep(2)
    print('message sent',i)
'''

'''
from kafka import KafkaProducer
from time import sleep
import json
from datetime import datetime


f=open("task1_file.txt")
p=f.readlines()
p=list(map(lambda x:x.strip(),p))
print(p)

producer=KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10,1))

producer.send('youtube',b'greetings@')

# a=format(1,'b')
# producer.send('msg',a)

# print(producer)



now=datetime.now()
# datetime.datetime()

current_time=now.strftime("%d/%m%Y %H:%M:%S")

print(current_time)



for i in range(len(p)):
    
    message='Messages {}'.format(format(p[i],'b'))
    producer.send('youtube',json.dumps(message).encode('utf-8'))
    sleep(2)
    print('message sent',i)

'''

'''
from kafka import KafkaProducer
from time import sleep
import json
from datetime import datetime
f=open("task1_input.txt")
p=f.readlines()
p=list(map(lambda x:x.strip(),p))
# print(p)

producer=KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10,1))

producer.send('youtube',b'welcome..')

# a=format(1,'b')
# producer.send('msg',a)

# print(producer)



now=datetime.now()
# datetime.datetime()

current_time=now.strftime("%d/%m%Y %H:%M:%S")

print(current_time)

a=[]

for i in range(len(p)):
    message='{}'.format(format(int(p[i]),'b'))
    a.append(message)
    producer.send('youtube',json.dumps(message).encode('utf-8'))
    sleep(2)
    print(p[i])


with open('solution-task1.txt', 'w') as f:
    
    f.writelines("%s\n" % length for length in a)

'''

'''
from kafka import KafkaProducer
from time import sleep
import json
from datetime import datetime

producer=KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10,1))

producer.send('youtube',b'1')

# a=format(1,'b')
# producer.send('msg',a)

# print(producer)



now=datetime.now()
# datetime.datetime()

current_time=now.strftime("%d/%m%Y %H:%M:%S")

print(current_time)



for i in range(10):
    message='Messages {}'.format(str(datetime.now().time()))
    producer.send('youtube',json.dumps(message).encode('utf-8'))
    sleep(2)
    print('message sent',i)
'''

'''
from kafka import KafkaProducer
from time import sleep
import json
from datetime import datetime


f=open("task1_file.txt")
p=f.readlines()
p=list(map(lambda x:x.strip(),p))
print(p)

producer=KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10,1))

producer.send('youtube',b'greetings@')

# a=format(1,'b')
# producer.send('msg',a)

# print(producer)



now=datetime.now()
# datetime.datetime()

current_time=now.strftime("%d/%m%Y %H:%M:%S")

print(current_time)



for i in range(len(p)):
    
    message='Messages {}'.format(format(p[i],'b'))
    producer.send('youtube',json.dumps(message).encode('utf-8'))
    sleep(2)
    print('message sent',i)

'''

'''

from kafka import KafkaProducer
from time import sleep
import json
from datetime import datetime
f=open("task1_input.txt")
p=f.readlines()
p=list(map(lambda x:x.strip(),p))
# print(p)

producer=KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10,1))

producer.send('consumer',b'welcome..')

# a=format(1,'b')
# producer.send('msg',a)

# print(producer)



now=datetime.now()
# datetime.datetime()

current_time=now.strftime("%d/%m%Y %H:%M:%S")

print(current_time)

a=[]

for i in range(len(p)):
    message='{}'.format(format(int(p[i]),'b'))
    a.append(message)
    producer.send('consumer',json.dumps(message).encode('utf-8'))
    sleep(2)
    print(p[i])


with open('solution-task1.txt', 'w') as f:
    
    f.writelines("%s\n" % length for length in a)

'''


from kafka import KafkaProducer
from time import sleep
import json
from datetime import datetime
file=open("task1_input.txt")
file_data=file.readlines()
file_data=list(map(lambda x:x.strip(),file_data))


producer=KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10,1))

producer.send('consumer',b'welcome..')

now=datetime.now()

current_time=now.strftime("%d/%m%Y %H:%M:%S")


print(current_time)


a=[]

def list_length(file_data):

    counter = 0
    for char in file_data:
        counter += 1
    return counter


for i in range(list_length(file_data)):
    message='{}'.format(format(int(file_data[i]),'b'))
    a.append(message)
    producer.send('consumer',json.dumps(message).encode('utf-8'))

    sleep(2)
    print("message ",file_data[i])

with open('solution_1_task.txt', 'w') as f:
     
    f.writelines("%s\n" % length for length in a)

