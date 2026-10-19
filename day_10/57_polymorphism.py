class dog:
    def sound(self):
        return "dog---bark"
class cat:
    def sound(self):
        return "cat---meow"
def animal_sound(animal):
    return animal.sound()
animal1=dog()
animal2=cat()
print(animal_sound(animal1))
print(animal_sound(animal2))

