# f = open("test.txt",'w')
# write_data = f.write("hello world\n")
# print(write_data)
# f.close()

# f = open("test.txt",'r')
# read_data = f.readlines()
# for i in read_data:
#     print(i)  
# print(read_data)
# f.close()

with open("test.txt",'w') as v:
    v.write("jai shree ram")
f= open("test.txt")
read_data = f.read()
print(read_data)
f.close()
