# a = int(input("enter you age: "))
# if a<18:
#     print("you are not eligible to vote ")
# elif a>=18 and a<60:
#     print("you are eligible to vote")

# a = int(input("Enter a number1: "))
# b = int(input("Enter a number2: "))
# c = int(input("Enter a number3: "))
# d = int(input("Enter a number4: "))

# if a>b or a>c and a>d:
#     print("a is the largest number: ",a)
# elif b>a and b>c and b>d:
#     print("b is the largest number: ",b)
# elif c>a and c>b and c>d:
#     print("c is the largest number: ",c)
# elif d>a and d>b and d>c:
#     print("d is the largest number: ",d)

marks1 = int(input("Enter marks1: "))
marks2 = int(input("Enter marks2: "))
marks3 = int(input("Enter marks3: "))

total_percentage = ((marks1+marks2+marks3)/300)*100
if (total_percentage >=40 and marks1>=33 and marks3>=33 and marks2>=33):
    print("you are pass",total_percentage)
else:
    print("you are fail")
