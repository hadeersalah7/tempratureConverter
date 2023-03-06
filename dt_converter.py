

def temp(c):
    msg1 = " Degrees Celsuis are "
    msg2 = " degrees Ferhnheight"
    result = (c * 9/5) + 32
    return str(c) + msg1 + str(result) + msg2

msg = input("Please enter temperture degrees in Celsuis")
fer_result =  temp(float(msg))
print(fer_result)    

if(float(msg) > 30):
    print("It's too hot! O.o")

print("Program shut down successfully! xD")


