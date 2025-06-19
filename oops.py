# class Student:
#     def __init__(self):
#         self.name = "Aditya"
#         self.age = 21

# display = Student()
# print(display.name)
# print(f"name of student is {display.name}\nand age is {display.age}")
# # print(display.regno)


# class Calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
# a= int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# obj = Calculator(a,b)

# print("sum of a and b is :",obj.add(a,b))

    
# class Rectangle:
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b
#     def area(self,l,b):
#         return l*b
#     def parameter(self,l,b):
#         return 2*(l+b)
# l = int(input("Enter the length: "))
# b = int(input("Enter the breadth: "))
# obj = Rectangle(l,b)
# print("area:-",obj.area(l,b))
# print("parameter:-",obj.parameter(l,b))
        

# class Student:
#     def __init__(self,name,roll,marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks
#     def result(self):
#         if self.marks>40:
#             print("pass")
#         else:
#             print("fail")
# obj = Student("aditya",20,55)
# obj.result()

# # class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def display_info(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Price: ${self.price}")
# book1 = Book("1984", "George Orwell", 15.99)
# book1.display_info()
# book2 = Book("To Kill a Mockingbird", "Harper Lee", 10.99)
# book2.display_info()    
# book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 12.99)
# book3.display_info()

class Movie:
    def __init__(self, name, rating,year):
        self.name = name
        self.rating = rating
        self.year = year
    def display_info(self):
        print(f"Title: {self.name}, Rating: {self.rating}, Year: {self.year}")
moive1 = Movie("omg", 8.8, 2015)
movie2 = Movie("omg2", 9.0, 2023)
moive1.display_info()
movie2.display_info()  
# create list and append it to movie
movie_list = []
movie_list.append(movie1)
movie_list.append(movie2)





