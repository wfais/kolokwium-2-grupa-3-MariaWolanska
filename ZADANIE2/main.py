from abc import ABC, abstractmethod

# Zdefiniuj abstrakcyjną klasę Animal
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Zdefiniuj klasę LandAnimal dziedziczącą po Animal
class LandAnimal(Animal):
    def make_sound(self):
        return "LandAnimal sound"

# Zdefiniuj klasę WaterAnimal dziedziczącą po Animal
class WaterAnimal(Animal):
    def make_sound(self):
        return "WaterAnimal sound"

# Zdefiniuj klasę Amphibian dziedziczącą wielokrotnie po LandAnimal i WaterAnimal
class Amphibian(LandAnimal, WaterAnimal):
    def make_sound(self):
        land_sound = LandAnimal.make_sound(self)
        water_sound = WaterAnimal.make_sound(self)
        return f"{land_sound} & {water_sound}"

if __name__ == '__main__':
    # Przykładowe wywołania:
    land = LandAnimal()
    water = WaterAnimal()
    frog = Amphibian()

    print("LandAnimal:", land.make_sound())  # "LandAnimal sound"
    print("WaterAnimal:", water.make_sound())  # "WaterAnimal sound"
    print("Amphibian:", frog.make_sound())  # "LandAnimal sound & WaterAnimal sound"