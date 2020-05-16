import random

def main():
    kerrigan = Baneling()
    arthas = Battlecruiser()
    fight_to_the_death(kerrigan, arthas)


def fight_to_the_death(red: 'Unit', blue: 'Unit'):
    print("Today! Fighting to the death, for your entertainment, we have.")
    print(f"In the red corner: {red}")
    print(f"In the blue corner: {blue}")

    while red.hp > 0 and blue.hp > 0:
        attack_first = random.choice([red, blue])
        if attack_first == red:
            attack_second = blue
        else:
            attack_second = red

        attack_first.attack_other(attack_second)

        if red.hp <= 0 or blue.hp <= 0:
            break

        attack_second.attack_other(attack_first)


    print()
    print("--- THE JUDGE'S SCORECARDS ---")
    print(f"red: {red}")
    print(f"blue: {blue}")

class Unit:
    hp: int
    max_hp: int
    attack: int

    def attack_other(self, other_unit: 'Unit'):
        print(f"{self} is attacking {other_unit}.")
        damage = self.attack
        if random.randint(1, 100) <= 5:
            print("It's a critical hit!")
            damage = damage * 2
        other_unit.hp -= damage
        if other_unit.hp <= 0:
            print(f"{other_unit} has been killed by {self}.")
            other_unit.hp = 0

class Battlecruiser(Unit):
    def __init__(self):
        self.max_hp = 10000
        self.hp = self.max_hp
        self.attack = 40

    def __str__(self):
        return f"<Battlecruiser {self.hp}/{self.max_hp} HP, {self.attack} attack>" 

class Baneling(Unit):
    def __init__(self):
        self.max_hp = 10000
        self.hp = self.max_hp
        self.attack = 40

    def __str__(self):
        return f"<Baneling {self.hp}/{self.max_hp} HP, {self.attack} attack>"

class Marine(Unit):
    def __init__(self):
        self.max_hp = 40
        self.hp = self.max_hp
        self.attack = 8
    
    def __str__(self):
        return f"<Marine {self.hp}/{self.max_hp} HP, {self.attack} attack>"

if __name__ == "__main__":
    main()
