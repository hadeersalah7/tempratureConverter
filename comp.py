# weather = input("Please insert the weather status! ")
# temperture = input("Please insert the tempertature status! ")

# if weather == "raining" and temperture == "cold":
#     print("Take an umberlla and a warm jacket")

# elif weather == "raining" and temperture == "warm":
#     print("take an umberlla and a t-shirt")

# elif weather == "sunny"  and temperture == "cold":
#     print("take a sunglasses and a jacket")   

# elif weather == "sunny"  and temperture == "warm":
#     print("Take a sunglasses and t-shirt")

# else: 
#     print("Just stay HOME! O.o")

# lang1 = "Python"
# lang2 = "JavaScript"
# numb1 = 12
# color = "blue"

# if lang1 == "Python" and lang2 == "JavaScript":
#     print("This is the thinking & creating course! xD")
# elif lang1 == "Python" or lang2 == "JavaScript":  
#     print("This is a good course!")
# elif numb1 <= 10 or color == "blue":
#     print("The test is true!")
# elif numb1 <= 10 and color == "blue":
#     print("The test is okay O.o")

# secret_numb = 17
# secret_col = "Teal"
# secret1 = input("Please enter a number between 1 ~ 20 ")
# secret2 = input("Please enter a color! ")

# if(secret_numb == int(secret1) and secret_col == secret2):
#     print("You've found both the secret color & the secret number! xD")
# elif (int(secret_numb) == secret1 or secret_col == secret2):
#     print("You found at least one of the secrets! O.o")    
# else:
#     print("You didn't find any of the secrets!")    
#     print("Better Luck next time! O.o")

# print("Try again?!")     


# // Defining Errors:

# def greet(name, age):
#     message = "Your name is " + name + " and you are " + age + " years old."
#     return message

# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print(greet(name, age))

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# num_one = input("Enter a number: ")
# num_two = input("Enter another number: ")

# message = "The result of " + str(num_one) + "  " + str(num_two) + " is " + str(add(int(num_one), int(num_two)))
# print(message)

# message = "The result of " + str(num_two) + " - " + str(num_one) + " is " + str(subtract(int(num_one, num_two)))
# print(message)

def get_result(answer):
    if answer == "a":
        return  True
    else:
        return False

print("Do you like programing?")
print("a. Yes")
print("b. No")
result = input("Enter a or b: ")

if get_result(result):
    print("Awesome! Programming is really fun!")
else:
 print("Hang in there! It's an acquired taste!")

