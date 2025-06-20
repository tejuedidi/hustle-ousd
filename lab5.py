# Lab 5 Teju Edidi

# Step 1
def cat_greeting(word):
    print(f'Cat says {word}')
    print('Cat says nothing')

cat_greeting("mee")

# Step 2
def generate_superhero_power():
    name = "Johnny"
    power = "flying"
    print(f"{name}'s power is {power}")

generate_superhero_power()

# Step 3
def generate_superhero_power1():
    power = "Flying"
    return power

print(generate_superhero_power1())

# Step 4
def generate_superhero_power2(user_name, super_power):
    message = user_name + " has the power of " + super_power + "!"
    return message

print(generate_superhero_power2("manica", "super human strength"))

# Step 5
def cat_greeting_loop():
    # for i in range(5):
    #     print(f'The cat says {greeting}')

    greetings = ["meow", "mo", "Meoiiw", "pur", "screech"]

    for i in greetings:
        print(" The cat says", i)

cat_greeting_loop()

# Step 6
def generate_multiple_powers():
    powers = ["Flying", "Super Strength", "Invisibility"]
    for power in powers:
        print(power)
generate_multiple_powers()