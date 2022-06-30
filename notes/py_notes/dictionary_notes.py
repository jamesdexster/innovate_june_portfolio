my_cat = {
    "name":"Jack",
    "colour":"Black",
    "mood":"lazy",
}
# key value pairs "":"", contains {} brackets
# do not have numbered index

print(my_cat["mood"]) # to find specific attributes you have to specify its main value

print(f"My cats name is {my_cat['name']}")
# quotations and single quotes both needed to seperate value and string

my_cat['mood'] = "hungry" # use this method to update value

print(my_cat.keys()) # keys method prints main values

# list example

my_list = ["hi","hello","hi","goodbye"]

list_count = my_list.count("hi")

my_list.append("hi")

print(my_list)
print(list_count) # list count doesnt recognise append method because variable was defined beforehand

# dictionary example

cat_keys = my_cat.keys() # creating a variable for dictionary keys
my_cat["age"]= 5 # adding a new main value and its value to dictionary
print(cat_keys)

print(my_cat.values()) # shows values of each individual key
print(my_cat.items()) # shows both keys and values
print(my_cat.get("mood")) # returns the data as none if it doesnt exist, avoiding fatal error
print(my_cat["mood"]) # also returns the value of key however if the key doesnt exist fatal error recieved

print(list(my_cat.keys())) # prints the dictionary keys in a list

for i in my_cat.keys():
    print(i) # for loop for amount of keys, outputs values as strings

my_cat.update({"legs":"4"}) # updates dictionary, key:value
my_cat.update({"name":"Jack Jack"}) # can be used to update existing key and value
my_cat.pop("legs") # used to remove keys





