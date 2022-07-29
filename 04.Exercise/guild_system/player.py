class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = self.DEFAULT_GUILD

    def add_skill(self, new_skill, mana_cost):
        if new_skill in self.skills:
            return f"Skill already added"

        self.skills[new_skill] = mana_cost
        return f"Skill {new_skill} added to the collection of the player {self.name}"

    def player_info(self):
        result = f"Name: {self.name}\n"
        result += f"Guild: {self.guild}\n"
        result += f"HP: {self.hp}\n"
        result += f"MP: {self.mp}\n"

        for skill, mana_cost in self.skills.items():
            result += f"==={skill} - {mana_cost}\n"

        return result.strip()
