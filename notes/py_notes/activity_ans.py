# FIRST ACTIVITIES

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

# -------------------------------------

# SECOND ACTIVITIES

# ACTIVITY 1

correct_choice = False
while correct_choice == False:
    user_num = input("Please enter a number...")
    try:
        print(int(user_num), "is your number" )
        print(type(int(user_num))) # prints data type
        correct_choice = True
    except:
        print(f"please enter a number, try again...")
        correct_choice = False

# ACTIVITY 2

countries = {
    "United Kingdom":"London",
    "France":"Paris",
    "Germany":"Berlin",
    "Spain":"Madrid",
    "Italy":"Rome",
}

countries.setdefault("USA","Washington D.C")
countries.setdefault("Norway","Olso")
# countries.update({"USA":"Washington D.C", "Norway":"Olso"})

for i in countries.items():
    print(i)

print("\n")

# I prefer to use this method to print keys and values because its the cleanest looking output

countries.update({
    "United Kingdom":"English",
    "France":"French",
    "Germany":"German",
    "Spain":"Spanish",
    "Italy":"Italian",
    "USA":"English",
    "Norway":"Norwegian"})
for i in countries.items():
    print(i)

# ACTIVITY 3

fav_music = [
    "Nirvana - Lithium",
    "System of a down - Chop Suey!",
    "Linkin Park - Numb",
]

list_songs = [
    {"artist":"Nirvana",
    "song_name":"Lithium",
    "genre":"Alternative",
    "release_year":"1992"},
    {"artist":"System of a Down",
    "song_name":"Chop Suey!",
    "genre":"Metal",
    "release_year":"2001"},
    {"artist":"Linkin Park",
    "song_name":"Numb",
    "genre":"Alternative",
    "release_year":"2003"},
]

# each dictionary is defined by index position in the list

for i in list_songs:
    print(i)
    print("\n")
# used to print all dictionaries inside list
# print(list_songs)

for i in list_songs[0].items():
    print(i)

print("\n")
# used to print individual dictionary using index postion

list_songs[0].update({"artist":"James"})
# updated [0], artist value
for i in list_songs[0].items():
    print(i)

print("\n")

list_songs.append(
    {"artist":"Red Hot Chilli Peppers",
    "song_name":"Californication",
    "genre":"Rock",
    "release_year":"1999"}
)
# used append method to add another dictionary to the end of the list

for i in list_songs:
    print(i, "\n")

del(list_songs[1]) # used del function to remove index [1] from the list

for i in list_songs:
    print(i)
    print("\n")

