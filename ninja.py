from pets import Pet
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

# implement the following methods:
    def walk(self): # walk() - walks the ninja's pet invoking the pet play() method
        self.pet.play()
        print(f"{self.first_name} is walking {self.pet.name}")
    def feed(self): # feed() - feeds the ninja's pet invoking the pet eat() method
        self.pet.eat()
        print("Craig is eating!")
    def bathe(self): # bathe() - cleans the ninja's pet invoking the pet noise() method
        self.pet.noise()
        print("Craig is bathing and making noise!")


craig = Pet()
sabrina = Ninja("Sabrina", "Henrice", "Pupperoni", "Blue Buffalo", craig)

sabrina.walk()
sabrina.feed()