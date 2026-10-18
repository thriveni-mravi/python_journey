class animal:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        return f"{self.name} makes a generic animal sound"
    def move(self):
        return f"{self.name} is playing"
class dog(animal):
    def make_sound(self):
        return f"{self.name} is barking"
    def fetch(self,item):
        return f"{self.name} is fetched the {item} "
class puppy(dog):
    def play(self):
        return f"{self.name} is playing with its mother"
    def sleep(self):
        return f"{self.name} is sleeping with its siblings"
    
generic_animal=animal("creature")
my_dog=dog("raja")
my_puppy=puppy("silky")

print(generic_animal.make_sound())
print(generic_animal.move())
print("\n",my_dog.make_sound())
print(my_dog.fetch("ball"))
print("\n",my_puppy.play())
print(my_puppy.sleep())
        
    