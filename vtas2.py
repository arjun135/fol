'''
f=open("names.txt")
p=f.readlines()
print(p)
temp=0
count=0
for i in range(0,len(p)):
    for j in range(0,len(p)):
        if(p[j]>p[i]):
            temp=p[i]
            p[i]=p[j]
            p[j]=temp
 '''           
    # for s in p[i]:
    #     count=count+1
    # print(p[],' ',count)    
        
def main():
    f=open("names.txt")
    p=f.readlines()
    # print(p)
    temp=0
    count=0
    for i in range(0,len(p)):
        for j in range(0,len(p)):
            if(p[j]>p[i]):
                temp=p[i]
                p[i]=p[j]
                p[j]=temp
    print(p)
    # inc=0
    
    for n in range(len(p)):
        print(p[n],length_count(p[n]))
 
        
        # p1=p[inc]
        
        
        # inc+=1
        # print(p1,length_count(p1))

def length_count(i):
    coun=-1
    for j in i:
        coun+=1
    return coun    






'''

        for j in p1:
            if j=='':
                break
            cou+=1
        'print(f"{p1}  --  {cou}".format(p1,cou))    '
        print(p1,end=" ")
        print(cou,end="")
        
    
        # if p=='':
        #     return 0
        # else:

'''

        # print(p, "  ", string(p))
    
# def string(p):
#     if p=='':
#         return 0
#     else:
#         return 1+string(p[1:])
        
main()


# p1=p.to_csv("output.hdf5")
# print(p1)
# for i in p:
#     print(i,end="")




print(p)
str(input("Enter the string: "))
with open('out.hdf5', 'w') as f:
    # web_browsers = ['Firefox\n', 'Chrome\n', 'Edge\n']
    f.writelines("%s\n" % line for line in p)