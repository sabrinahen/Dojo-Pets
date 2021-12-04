class Pet:
    def __init__(self, name = "Craig" , type = "Corgi" , tricks = "Rollover"):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 50
        self.energy = 50

# implement the following methods:
    def sleep(self): # sleep() - increases the pets energy by 25
        self.energy += 25
        print(f"{self.name} is sleeping and his energy is now {self.energy}")
    def eat(self): # eat() - increases the pet's energy by 5 & health by 10
        self.health += 10
        self.energy += 5
        print(f"{self.name} is eating. His energy is {self.energy} and his health is {self.health}")
    def play(self): # play() - increases the pet's health by 5
        self.health += 5
    def noise(self): # noise() - prints out the pet's sound
        print("Oink Oink!")

# class Ninja:
#     def __init__(self, first_name, last_name, treats, pet_food, pet):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.treats = treats
#         self.pet_food = pet_food
#         self.pet = pet

# # implement the following methods:
#     def walk(self): # walk() - walks the ninja's pet invoking the pet play() method
#         self.pet.play()
#         print(f"{self.first_name} is walking {self.pet}")
#     def feed(self): # feed() - feeds the ninja's pet invoking the pet eat() method
#         self.pet.eat()
#         print("Craig is eating!")
#     def bathe(self): # bathe() - cleans the ninja's pet invoking the pet noise() method
#         self.pet.noise()
#         print("Craig is bathing and making noise!")


# craig = Pet()
# sabrina = Ninja("Sabrina", "Henrice", "Pupperoni", "Blue Buffalo", craig)

# craig.sleep()
# sabrina.feed()
