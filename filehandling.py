# f = open("test.txt",'w')
# write_data = f.write("hello world\n")
# print(write_data)
# f.close()

f = open("test.txt",'r')
read_data = f.readlines()
for i in read_data:
    print(i)  
print(read_data)
f.close()