#program 7 anudip foundation
# using while loop - it is used when no. of iterations are not known 
print("number between 100 and 1000 divisble by 3 and are even:")
x=100 #value is initialized for while loop
count=0 
while(x<1000): #condition to exit the loop
    if(x%2==0 and x%3==0):
        print(x ," , ",end="")
        count=count+1 
    x=x+1   #value is updated
print("\n total possible numbers are:",count)
