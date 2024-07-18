#program 4 anudip foundation
#implementing nested conditional statement through example of profit and loss

cp = float(input("enter your cost price"))   #taking cost price and selling price as an input from user
sp = float(input("enter your selling price"))
if(cp<0):                              #cost price and selling price cant be 0 hence condition is provided to check it , program will terminate if cp or sp =0.
    print("cost price is invalid")
elif(sp<0):
    print("selling price is invalid")
else:                             #if selling price is greater than it shows profit .
    if(sp>cp):
        print("Profit: Rs" , (sp-cp))  #profit is calculated
    elif(cp>sp):
         print("Loss: Rs" , (cp-sp))  #if cp is greater it indicates loss , here loss is calculated . this condition will run only in case when if condition is false.
    else:
        print("No profit, No Loss") # if sp=cp , there is no loss or profit
