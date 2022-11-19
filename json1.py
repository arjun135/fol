import json
data = '{"var1":"harry","var2":34}'
parsed=json.loads(data)
print(parsed['var1'])
print(type(parsed))
print(parsed)

data2='{"mysql_ip":"127.0.0.1","port" : "3306","username" : "arjun","password" : "12345","cars":["bmw","OOOO"]}'

parsed=json.loads(data2)


pad=json.dumps,(data2)
print(pad)
# print(parsed)



























