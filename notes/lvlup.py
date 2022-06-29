# int, float, str - casting examples

# truthy and falsey, 0, empty strings or false would be falsey

# def add_up():
#     num1 = input("What is the first number you'd like to add up? \n")
#     num2 = input("What is the second number you'd like to add up? \n")

#     try:
#         print(int(num1) + int(num2))
#     except:
#         print("Please use numbers only")
#         print("try again")
#         add_up()
# add_up()

# try and except allows me to write my own error without fatal errors

# light = False # variables outside of function are naturally global
# def light_switch():
#     global light # allows the local variables inside the function to become global
#     if light: # if light is true
#         print("Whoa! Its bright in here")
#         light = False
#     else:
#         print("Who turned out the lights?")
#         light = True
# light_switch()
# light_switch()

# odd_num = [1,2,3,4,5,6,7,8,9,0] # list
# even_num = (1,2,3,4,5,6,7,8,9,0) # tuple

# # tuples are unchangable via methods once its been created
# odd_num.append(12)
# odd_num.insert(2,4) # inserts item into list, place,item
# print(odd_num)

# fav_music = [
#     "Nirvana - Lithium",
#     "System of a down - Chop Suey!",
#     "Linkin Park - Numb",
#     "HI",
#     "Yo",
# ]

# print(fav_music[1])
# print(fav_music[0:5:1]) # start, stop, step

# test = "Maxam"

# if test.lower() == test.lower()[::-1]:
#     print(f"Yes! {test} is a palindrome")
# else:
#     print(f" {test} is not a palindrome")

# # This while loop runs under a condition, it will continue onwards if the condition is not met

# import random
# num= 3
# while num%2==0:
#     print("We like even numbers! Another!")
#     num=random.randint(1,50)
# # If odd, the loop wont run
# print("Oh no! An odd number!") 

# # This while loop will always run

# while True:
#     num=random.randint(1,50)
#     print(num)
#     if num %2==0:
#         print("We like even numbers! Another!")
#         continue
#     else:
#         print("An add number!")
#         break












