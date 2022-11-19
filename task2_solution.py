'''
f=open("names.txt")
p=f.readlines()
# print(p)
temp=0

for i in range(0,len(p)):
    for j in range(0,len(p)):
        if(p[j]>p[i]):
            temp=p[i]
            p[i]=p[j]
            p[j]=temp  


p=list(map(lambda x:x.strip(),p))
# print(p)
b=[]
p2=[]
a=[]
rn=[]
for i in range(len(p)): 
    co=0
    p1=p[i]
    
    
    p2.append(p1)
    for j in p1.replace(" ",""):
        co+=1
    a.append(co)

with open('Output_names.txt', 'w') as f:
   
    f.writelines("%s\n" % names for names in p2)


with open('lengths.hdf5', 'w') as f:
    
    f.writelines("%s\n" % length for length in a)

'''

'''

f=open("names.txt")
p=f.readlines()
# print(p)
temp=0

k=0
for i in p:
    k+=1



# def length(p):
#    return sum(map(lambda x:1, p))

# print(length(p))



for i in range(0,k):
    for j in range(0,k):
        if(p[j]>p[i]):
            temp=p[i]
            p[i]=p[j]
            p[j]=temp  


p=list(map(lambda x:x.strip(),p))
# print(p)
b=[]
p2=[]
a=[]

def list_length(my_string):

    counter = 0
    for char in my_string:
        counter += 1
    return counter



for i in range(list_length(p)): 
    co=0
    p1=p[i]
    
    
    p2.append(p1)
    for j in p1.replace(" ",""):
        co+=1
    a.append(co)

with open('Output_names.txt', 'w') as f:
   
    f.writelines("%s\n" % names for names in p2)


with open('lengths.hdf5', 'w') as f:
    
    f.writelines("%s\n" % length for length in a)


'''

file=open("names.txt")
file_data=file.readlines()
# print(file_data)
temp=0

length_of_list=0
for i in file_data:
    length_of_list+=1

for i in range(0,length_of_list):        # Sorting names
    for j in range(0,length_of_list):
        if(file_data[j]>file_data[i]):
            temp=file_data[i]
            
            file_data[i]=file_data[j]
            file_data[j]=temp  


file_data=list(map(lambda x:x.strip(),file_data))
# print(file_data)
file_data_sort=[]


def list_length(my_string):

    counter = 0
    for char in my_string:
        counter += 1
    return counter


count_of_length=[]
for i in range(list_length(file_data)): 
    count=0
    file_data_index=file_data[i]
    
    
    file_data_sort.append(file_data_index)
    for j in file_data_index.replace(" ",""):
        
        count+=1
    count_of_length.append(count)

with open('Output_names.txt', 'w') as f:
   
    f.writelines("%s\n" % names for names in file_data_sort)


with open('lengths.hdf5', 'w') as f:
    
    f.writelines("%s\n" % length for length in count_of_length)


