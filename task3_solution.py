file=open("input.txt")
file_data=file.readlines()

file_data=list(map(lambda x:x.strip(),file_data))
# print(file_data,type(file_data))

even_number=[i for i in file_data if int(float(i))%2!=1]
# even_number = [num for num in file_data if int(float(num)) % 2 == 0]
# even_number=[i for i in file_data ]
# print(even_number)

with open('input.txt', 'w') as f:
    f.writelines("%s\n" % i for i in even_number)


import numpy as np
id=np.array(even_number)

with open('even_number_1D.hdf5', 'w') as f:
    f.writelines("%s\n" % length for length in id)






