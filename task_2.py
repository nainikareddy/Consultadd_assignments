def divisibility_test(num):
    if num % 3 == 0 and num % 5 == 0:
        print("Consultadd Python Training")
    elif num%5 == 0:
        print("Python Training")
    elif num%3 == 0:
        print("Consultadd")
    else:
        return None
def user_input_action(uinput):
    print("Enter 2 numbers")
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    if uinput == 1:
        #print("Im hete")
        if (num1+num2) > 0:
            print(num1 + num2)
        else:
            print("Negative")
    elif uinput == 2:
        if(num2-num1) > 0:
            print(num2-num1)
        else:
            print("Negative")
    elif uinput == 3:
        if (num2/num1) > 0:
            print(num2/num1)
        else:
            print("Negative")
    elif uinput == 4:
        if (num2*num1) > 0:
            print(num2*num1)
        else:
            print("Negative")
    elif uinput == 5:
        num3 = int(input("Enter another number:"))
        num4 = int(input("Enter one more number:"))
        print((num1+num2+num3+num4)/4)
    else:
        print("No action to perform")


#action = int(input("Enter a number 1-5 to choose an action"))
#user_input_action(action)
x = 1
while x <5:
    print(x)
    x+= 1
    if x == 3:
        break
    else:
        print("Error")
