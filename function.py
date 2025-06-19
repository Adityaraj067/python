# Write a function get_max(num1, num2) that returns the maximum of the two numbers.
# def get_max(num1, num2):
#     if num1>num2:
#         return num1
#     else:
#         return num2
# # a = get_max(10,20)
# a = int(input("Enter a number1: "))
# b = int(input("Enter a number2: "))
# c = get_max(a , b)

# print(c)


# Write a function count_vowels(s) that returns the number of vowels in the given string.
# Input: "Hello World"
# Output: 3

# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count
# s = input("Enter a string: ")
# print(count_vowels(s))


# Write a function sum_numbers(lst) that returns the sum of all numbers in a list.
# Input : [1,2,3,4,5]
# Output : 15

# def sum_numbers(lst):
#     return sum(lst)
# print(sum_numbers([1,2,3,4,5]))


# Write a function word_frequency(sentence) that returns a dictionary with word frequency.
# Input: "this is a test this is not fun"
# Output: {'this': 2, 'is': 2, 'a': 1, 'test': 1, 'not': 1, 'fun': 1}

def word_ferequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] +=1
        else:
            frequency[word] = 1
    return frequency
sentence = input("Enter a sentence: ")
print(word_ferequency(sentence))