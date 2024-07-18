#program 3 anudip foundation(multiple dependent conditions)
# implementing if-elif-else statement through the example of finding greater number
num1 = float(input("enter 1st number"))  #take two numbers as input from user
num2 = float(input("enter 2nd number"))
if(num1>num2):         #condition 1 : if first number input by user is greater than second number
    print("number 1 is greater than number 2")
elif(num1 == num2):          #condition 2: both number are equal , relational operator is used
    print("both numbers are equal")  
else:
    print("number 2 is greater than number 1")
