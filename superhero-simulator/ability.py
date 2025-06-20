# # # ability.py

# # import random

# # class Ability:
# #     def __init__(self, name, max_damage):
# #         '''Initialize the ability with a name and max_damage'''
# #         self.name = name
# #         self.max_damage = max_damage
    
# #     def attack(self):
# #         '''Return a random value between 0 and max_damage'''
# #         return random.randint(0, self.max_damage)

# # # Testing the Ability class
# # if __name__ == "__main__":
# #     fireball = Ability("Fireball", 50)
# #     print(fireball.attack())  # Test if attack() returns a random value between 0 and 50

















# # ability.py
# import random

# class Ability:
#     def __init__(self, name, max_damage):
#         self.name = name
#         self.max_damage = int(max_damage)
    
#     def attack(self):
#         return random.randint(0, self.max_damage)


# if __name__ == "__main__":
#     fireball = Ability("Fireball", 50)
#     print(fireball.attack())







# ability.py
import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name 
        self.max_damage = max_damage

    def attack(self):
        '''Return a random value between 0 and max_damage'''
        return random.randint(0, self.max_damage)    


# testing!
if __name__ == "__main__":
    fireball = Ability("Fireball", 20000)
    print(fireball.attack())
