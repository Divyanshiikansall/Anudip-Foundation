#program 4 anudip foundation

cp = float(input("enter your cost price"))
sp = float(input("enter your selling price"))
if(cp<0):
    print("cost price is invalid")
elif(sp<0):
    print("selling price is invalid")
else:
    if(sp>cp):
        print("Profit: Rs" , (sp-cp))
    elif(cp>sp):
         print("Loss: Rs" , (cp-sp))
    else:
        print("No profit, No Loss")
