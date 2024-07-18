#program 9 anudip foundation

print("number between 100 and 1000 divisble by 3 and are even:")
x=100
count=0
while(x<1000):
    if(x%2==0 and x%3==0):
        print(x ," , ",end="")
        count=count+1
    x=x+1
print("\n total possible numbers are:",count)
