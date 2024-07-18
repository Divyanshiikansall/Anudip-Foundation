#program 5 anudip foundation
#implementing for loop - it is used when number of iterations are known .

print("The number divisble by 10 and 7 between the number 10 to 500 are:")
for i in range (10,500): #10 is included and 500 is excluded
    if(i%10==0 and i%7==0): #logical operator is used to produce combine result of two conditions
        print(i)
