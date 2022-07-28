class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health -= damage

        if self.health - damage <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, amount):
        self.health += amount


batman = Hero("BruceWayne", 100)
print(batman.defend(101))
print(batman.heal(50))
print(batman.health)
