# ACTIVITY 1

welcome_msg = "Welcome to Code Nation"

msg_length = len(welcome_msg)
msg_length_even = len(welcome_msg)%2
if msg_length_even == 0:
    print(welcome_msg)
    print("welcome message length is even")
    print(msg_length, "is yout message length")
else:
    print(welcome_msg)
    print("Your message length isnt even")
    print(msg_length, "is your message length")

# ACTIVITY 2

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]
for i in alpha:
    print(i)

user_num = int(input("Choose and number between 1 and 25\n"))
user_num -= 1
print(alpha[user_num], "is what your number represents in the alphabet")

# ACTIVITY 3

player_n_and_c = str(input("Choose X or O"))
comp_n_and_c = "O"
if player_n_and_c == "O":
    print("You have choosen O")
    player_n_and_c == "O"
    comp_n_and_c == "X"
elif player_n_and_c == "X":
    print("You have choosen X")
    player_n_and_c == "X"
    comp_n_and_c == "O"
else:
    print("Please choose X or O")

