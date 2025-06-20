# # armor.py



































import random

class Armor:
    def __init__(self, name, max_block):
        '''Initialize the armor with a name and max_block value'''
        self.name = name
        self.max_block = max_block
    
    def block(self):
        '''Return a random value between 0 and max_block'''
        return random.randint(0, self.max_block)

# Testing the Armor class
if __name__ == "__main__":
    shield = Armor("Shield", 30)
    print(shield.block())  # Test if block() returns a random value between 0 and 30
