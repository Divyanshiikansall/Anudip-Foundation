#program 8 anudip foundation

total_num=0
print("total numbers between 100 to 1000 which are even and divisble be 3:")
for i in range(100,1000):
    if(i%2==0 and i%3==0):
        total_num+=1;
        print(i," , ",end="")
print("\n----------------------------------------------------------------------------------------------------------------------------")
print("\n total posible number satisfying the given condition:",total_num)
