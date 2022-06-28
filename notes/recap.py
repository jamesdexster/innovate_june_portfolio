print("This is my recap file")

greeting = "Hello Everyone" # variable greeting created and defined

print(greeting) # prints variable

print("This is a string displaying characters")
print("1234") # string
print(1234+1) # interger
print(0.01) # float
print(True) 
print(False) # boolean
print(None) #none - blank/null data

# git add .
# git commit - m ""
# git push -u origin main

# examples of properties
print(len(greeting))
print(greeting[1])
print(greeting[-2])
print(greeting.upper())
print(greeting.capitalize())
print(greeting.count("Hello"))
print(greeting.find("l"))
print(greeting.replace("Everyone","All"))
print(len("Hello      ".strip()))

# examples of random library and methods
import random
from random import randint, uniform
print(random.random())
print(random.uniform(1,10))
print(random.randint(1,10))

my_name = "James"
my_age = 19
student = False

print(my_name, my_age, student)
print("Hello my name is", my_name)
print("I am", my_age, "years old")

print("Hello my name is " + my_name)

# print("I am" + my_age) example of concatenation error

# format method examples
# used to implement variables

print("Hello my name is {} and I am {} years old".format(my_name,my_age)) # older format method

print(f"Hello my name is {my_name} and I am {my_age} years old") # newer format method


# examples of arithmetic operators
# print(1+2)
# print(1-2)
# print(1*2)
# print(1**2)
# print(1/2)
# print(1%2)

balance = 9999
print(balance)
amount = 1111

# balance = amount + balance
balance += amount

# balance = amount - balance
balance -= amount

#balance = amount * balance
balance *= amount

print(amount)
print(balance)

# example of input method
answer = input("What is your name? \n")
print(answer)

# example of if statement

music = "rock and roll"
if music == "rock and roll":
    print("Oh no! I cant hear myself think")
elif music == "no music":
    print("Ahh, peace and quiet")
else:
    print("U have great music taste")

music_choice = "incorrect"
while music_choice == "incorrect":
    music = input("What genre would you like?\nClassical, Rock or Pop...\n")
    if music.upper() == "CLASSICAL":
        print("Turn this off, noone at the party likes it")
        music_choice = "correct"
    elif music.upper() == "ROCK":
        print("The neighbours wont be very happy!")
        music_choice = "correct"
    elif music.upper() == "POP":
        print("Everyone likes your music!")
        music_choice = "correct"
    else:
        print("Wrong Input...\n")
        music_choice = "incorrect"

# examples of defining a variable

def music_selection():
    music_choice = "incorrect"
    while music_choice == "incorrect":
        music = input("What genre would you like?\nClassical, Rock or Pop...\n")
        if music.upper() == "CLASSICAL":
            print("Turn this off, noone at the party likes it")
            music_choice = "correct"
        elif music.upper() == "ROCK":
            print("The neighbours wont be very happy!")
            music_choice = "correct"
        elif music.upper() == "POP":
            print("Everyone likes your music!")
            music_choice = "correct"
        else:
            print("Wrong Input...\n")
            music_choice = "incorrect"
music_selection()

# example of using variables in parameters of def

def cash_withdrawal(amount, accnum):
    print(f"You have withdrawn {amount} from {accnum}")
cash_withdrawal(300, 123456)

fav_music = [
    "Nirvana - Lithium",
    "System of a down - Chop Suey!",
    "Linkin Park - Numb",
]
print(fav_music)

print(fav_music[0]) # index postion, target items in a list

print(len(fav_music))

fav_music.append("RHCP - Californication")
print(fav_music)  # add to list

fav_music.pop()
print(fav_music) # removes item from list, accepts index position in parameters


































