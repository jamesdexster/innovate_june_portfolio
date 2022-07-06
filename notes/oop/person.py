# Uppercase Class - Lowercase Function - .Method Method

class Person():
    def __init__(self, person_name, person_height, person_age): 
        # using this to set attributes - self keyword is used to relate the attributes to this specific class
        self.name = person_name # this is a attribute
        self.height = person_height
        self.age = person_age
    
    def set_hair(self, person_hair):
        self.hair = person_hair
    
    def get_hair(self):
        print(self.hair)

# npc_one = Person("James", 20)
# npc_two = Person("Katy", 30)


# print(npc_one.name)
# print(npc_two.name)
# print(npc_one.name,npc_one.course,npc_one.age)







