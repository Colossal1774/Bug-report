


def sum (a,b): 
    result = a+b
    return result

def subtract(a,b):
    result = a - b
    return result

def division(a,b):
    result = a * b
    return result

def multiplication(a,b):
    result = a * b
    return result

input1 = float(input("Въвеедете пръвото число "))
input2 = float(input("Въвеедете второто число "))
input3 = str(input("Изберете операция |+| |-| |*| |/|"))
if(input3 == "+"):
        print(sum(input1,input2))

elif(input3 == "-"):
        print(subtract(input1,input2))

elif(input3 == "/"):
        print(division(input1,input2))

elif(input3 == "*"):
        (multiplication(input1,input2))
else:
    print("Невалидна операция!")
