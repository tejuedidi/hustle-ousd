# Debugging Activity Teju Edidi

# Code Snippet 1: ---------
print("Code Snippet 1: ---------")
# encountered a zerodivisionerror comes up when dividing by 0, fixed by dividing by 5
x = 10
y = 5
result = x / y
print("Result:", result)




# # # # Case 2
# # # print("Case 2: ---------")
# # # numbers = [1, 2, 3, 4, 5]
# # # # index error list is not accessible bc now it is out of range, 
# # # for i in range(len(numbers)):
# # #    print(numbers[i])



# # # print("Case 3: ---------")
# # # # missing colon
# # # def calculate_area(radius):
# # #    area = 3.14 * radius ** 2
# # #    return area
 
# # # radius = 5
# # # print(calculate_area(radius))


# # # print("Case 9: -----------")
# # # name = input("Enter your name: ")
# # # if name == ("Alice" or "Bob"):
# # #    print("Hello, " + name)
# # # else:
# # #    print("Hello, stranger!")




# # # # # print("Case 4: ---------")
# # # # # # syntax missing colon
# # # # # def is_even(number):
# # # # #    if number % 2 == 0:
# # # # #        return True
# # # # #    else:
# # # # #        return False
 
# # # # # print(is_even(4))
# # # # # print(is_even(7))

# print("Case 9: ---------")
# # == operator needs one argument on the side
# name = input("Enter your name: ")
# age = 10
# if name == ("Alice" or "Bob"): # name == "Alice" or name == "Bob"
#    print(f"Hello,  {name} {age}")
# else:
#    print("Hello, stranger!")

# print("Case 10: ---------")
# def divide_numbers(x, y):
#    result = x / y
#    return result
 
# num1 = 10
# num2 = 5
# print(divide_numbers(num1, num2))


def greet(name):
   return "Hello, " + name
 
print(greet("Alice"))









name = input("Enter your name: ")
if name == ("Alice" or "Bob"): # if name == "Alice" or name == "Bob"
   print("Hello, " + name)
else:
   print("Hello, stranger!")


x == y