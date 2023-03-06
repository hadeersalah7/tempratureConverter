# password = "Amunet"
# guess_pass = input("Please enter your secret word! ")

# if(password == guess_pass):
#     print("Congratulations! You've found the secret word!")

# else:
#     print("Wrong guess! O.o")
#     print("Play again?")



# apples = 9
# oranges = 26 

# if(apples != oranges):
#     print("Not  quite!")

# result = 96
# quest = input("What is the output of 7 + 88 ")

# if(result == int(quest)):
#     print("Congratulations! You've found the right answer xD")

# print("The program terminated successflly!")


# def convert(money):
#     msg1 = " Egyptian Pounds are " 
#     msg2 = " US Dollars"
#     result = money * 30
#     return str(money) + msg1 + str(result) + msg2

# money_input = input("Please Enter The Amount You Want To Convert to")   

# money_convert = convert(float(money_input))

# if(float(money_input) > 50000):
#     print("That's A lot Of Money! O.o")

# print(money_convert)   
# print("Amount Converted Successfully! xD") 

# def convert(cm):
#     if cm < 0:
#         print("Beware! A negative value!")

#     msg1 = " centmetries are "   
#     msg2 = " inches. " 
#     result = cm / 2.54
#     return str(cm) + msg1 + str(result) + msg2

# input_msg = input("Please enter conversion")   

# msg3 = convert(float(input_msg))
# print(msg3)

# print("Success!")


# numb1 = input("Please enter a first number ")
# numb2 = input("Please enter a second number ")

# total = int(numb1) - int(numb2)

# if(int(total) > 10):
#     print("The number is greater than 10")

# elif(int(total) > 0):
#     print("The result is bigger than 0 but less than 10!")

# elif (int(total) == 0):
#     print("The result is 0! O.o")

# else:
#     print("The result is a negative number")  

# print("You Can try again!")      
# 

# weather = "sunny"
# temperture = "cold"
  
# if(weather == "sunny" and temperture =="warm"):
#     print("Take sunglasses and a t-shirt"

in1 = input("Please insert first number! ")
in2 = input("Please insert second number! ")

# res = int(in1) + int(in2)

if(int(in1) > 10 and int(in2) > 10):
    print("Both of the numbers are greater than 10! xD")
elif int(in1) > 10 or int(in2) > 10:
    print("At least one of the numbers you entered is not greater than 10! O.o")
