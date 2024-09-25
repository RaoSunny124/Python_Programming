number1:str = float(input("Enter the first number:"))
number2:str = float(input("Enter the second number:"))
operator = input("Enter the operator +,-,*,/ :")
if (operator == '+'):
    print(number1 + number2)
elif (operator == "-") :
    print(number1 - number2)
elif  (operator == "*") :
    print(number1 * number2)
elif (operator == "/") :
    print(number1 / number2)
else :
    print('invalid operator')      



