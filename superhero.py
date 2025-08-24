# superhero.py

class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        return f"Hi, I'm {self.name}, a superhero from {self.origin} with the power of {self.power}!"

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Example usage:
ironman = Superhero("Iron Man", "Flight and Laser Blasts", "Earth")
print(ironman.introduce())
ironman.use_power()
