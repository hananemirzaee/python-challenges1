# #--------------1--------------
# dict_user = {"name":"hana", "age":19, "student":True} 
# print(type(dict_user["name"])) 
# print(type(dict_user["age"])) 
# print(type(dict_user["student"])) 
 
# print("----------------OR----------------")
 
# list_user = ["hana", 19, "student"] 
# for i in list_user: 
#     print(i, type(i))


# #--------------2--------------
# while True:
#     number = input("Enter your number: ")
#     try:
#         number = int(number)
#     except ValueError as e:
#         print('ValueError:', e)
#     else:
#         break
        
# print("The square of this number is: ", number ** 2)


# # --------------3--------------
# while True:
#     num = input("Enter your number: ")
#     try:
#         num = float(num)
#         break
#     except ValueError as e:
#         print('ValueError:', e)
#         # continue

# if num > 0:
#     print("Your number is positive")
# elif num < 0:
#     print("Your number is negative")
# else:
#     print("Your number is zero")

# # --------------4--------------
# while True:
#     age = input("Enter your age: ")
#     try:
#         age = int(age)
#         break
#     except ValueError as e:
#         print('ValueError', e)
#         continue

# if age in range(18, 31):
#     print("adult")
# else:
#     print("Not valid")
    
# # --------------5--------------
# while True:
#     number1 = input("Enter your first number: ")
#     try:
#         number1 = float(number1)
#         break
#     except ValueError as e:
#         print('ValueError:', e)
#         continue

# while True:
#     number2 = input("Enter your second number: ")
#     try:
#         number2 = float(number2)

#        # Check zero division
#         if number2 != 0:
#             division_result = number1 / number2
#             break
#         else:
#             print("You cannot divide to zero")
#     except ValueError as e:
#         print('ValueError:', e)
#         continue

# sum_result = number1 + number2
# minus_result = number1 - number2
# multiply_result = number1 * number2

# print("sum: ", sum_result)
# print("minus: ", minus_result)
# print("multiply: ", multiply_result)
# print("division: ", division_result)

# # --------------6--------------
# while True:
#     temp = input("Enter your temperature: ")
#     try:
#         temp = int(temp)
#         break
#     except ValueError as e:
#         print('ValueError', e)

# if temp < 0:
#     print("Cold")
# elif 0 <= temp <= 35:
#     print("Normal")
# else:
#     print("Hot")

# # --------------7--------------
# number = 1
# while number <= 10:
#     print(number)
#     number += 1

# # --------------8--------------
# list_element = [10, 20, 30, 40, 50] 
# for i in list_element: 
#     print(i)

# print("--------------------OR--------------------")

# index = 0
# while index < len(list_element):
#     print(list_element[index])
#     index += 1

# # --------------9--------------
# while True:
#     num = input("Enter your number: ")
#     try:
#         num = int(num)
#         if num < 0:
#             print("Please enter a positive number")
#             continue
#         break
#     except ValueError as e:
#         print('ValueError', e)
#         continue 

# if num % 2 == 0:
#     print("The number is even", num)
#     for i in range(0, num + 1, 2):
#        print(i)
# else:
#     print("The number is odd", num)
#     for i in range(1, num + 1, 2):
#         print(i)


# # --------------10--------------
# while True:
#     number = input("Enter your number: ")
#     try:
#         number = int(number)
#         if number <= 0:
#             print("Please enter a positive number")
#             continue
       
#     except ValueError as e:
#         print('ValueError', e)
        

#     count = 1 
#     factorial = 1

#     while count <= number:
#         factorial *= count
#         count += 1
#     print("Your factorial is: ", factorial)
#     break

# # --------------11--------------
# list_1 = [10, 20, 30, 10]
# list_2 = [75, 0, 30, 35]

# if (list_1[0] == list_1[-1]):
#     print("list_1: True")
# else:
#     print("list_1: False")
    
# if (list_2[0] == list_2[-1]):
#         print("list_2: True")
# else:
#     print("list_2: False")
    
# # --------------12--------------
# list_divisible = [10, 20, 33, 46, 55]
# for i in list_divisible: 
#     if i % 5 == 0: 
#         print(i) 

# # --------------13--------------
# row = 5
# for i in range(1, row + 1):
#     print(str(i) * i)
