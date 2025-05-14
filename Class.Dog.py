class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def bark(self):
        return f"{self.name} says: Woof!"

    def describe(self):
        return f"{self.name} is a {self.age}-year-old {self.color} dog."

    def play(self):
        return f"{self.name} is playing fetch."

class JackRussell(Dog):
    def __init__(self, name, age, color, energy_level):
        super().__init__(name, age, color)
        self.energy_level = energy_level

    def play(self):
        if self.energy_level > 7:
            return f"{self.name} is zooming around the garden!"
        else:
            return f"{self.name} is too tired to play."

    def eat(self, food):
        self.energy_level += 2
        return f"{self.name} eats {food} and gains more energy!"

    def nap(self):
        self.energy_level = max(0, self.energy_level - 3)
        return f"{self.name} takes a nap and calms down."

coco = JackRussell(name="Coco", age=3, color="brown and white", energy_level=8)

# Simulate a day with Coco
print(coco.describe())         # Introduction
print(coco.bark())             # Bark!
print(coco.play())             # Coco plays
print(coco.eat("chicken"))     # Coco eats
print(coco.nap())              # Coco naps
print(coco.play())             # Coco plays again
