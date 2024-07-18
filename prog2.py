#program 2 anudip foundation
sec = int(input("Enter time in seconds : "))
if(sec>=0):
    hour =0
    minu =0
    if(sec >= 3600):
        hour = sec // 3600
        sec = sec % 3600
    if(sec >= 60):
        minu = sec // 60
        sec = sec % 60
    print(hour , " hours " , minu ,"minutes" , sec , "seconds")
else:
    print(" invalid time")
    
