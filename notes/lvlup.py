# int, float, str - casting examples

# truthy and falsey, 0, empty strings or false would be falsey

def add_up():
    num1 = input("What is the first number you'd like to add up? \n")
    num2 = input("What is the second number you'd like to add up? \n")

    try:
        print(int(num1) + int(num2))
    except:
        print("Please use numbers only")
        print("try again")
        add_up()
add_up()


# try and except allows me to write my own error


