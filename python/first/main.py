#variables
number =input("what is your number: ") 
number2 =input("What is your second number: ")
operator =input("+, -, *, /: ")

number_float = float(number)
number2_float = float(number2)

if (operator == "+"):
    print(number_float+number2_float)
elif (operator == "-"):
    print(number_float-number2_float)
elif (operator == "*"): 
    print(number_float*number2_float)
elif (operator =="/"): 
    print(number_float/number2_float)