# Lab 3 Teju Edidi

# Task 1: Strings
food = "cheese cake"

print("The first 3 characters of my food variable string:", food[0:3])
print("The last 3 characters of my food variable string:", food[-3:])

first_last = food[0] + food[-1]
print("The first characters + last character of my food variable string:", first_last)

split_str = food.split()
print("The split method", split_str)

print("The join method", "".join(split_str))


# Task 2: List
number_list = [1,2,2,3,4,5,6,7,8]
number_list.append(9)
number_list.insert(3, 7)

number_list.remove(2)
print(number_list)


# Task 3: Working with Dictionaries
books = {"Elisabetta Dami" : "Four Mice Deep in the Jungle", "Jannifer" : "Working in Python"}
print(books.keys())
print(books.values())
print(books.get("Jannifer"))