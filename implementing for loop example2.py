#program 9 anudip foundation
# for loop example 2
total_num=0 # used for counting total number which satisfy given condition
print("total numbers between 100 to 1000 which are even and divisble be 3:")
for i in range(100,1000): # 100 is included and 1000 is excluded , step value is 1.
    # forward indexing as positive numbers are used
    if(i%2==0 and i%3==0):
        total_num+=1;
        print(i," , ",end="") # to print all the numbers in the same line
print("\n----------------------------------------------------------------------------------------------------------------------------")
print("\n total posible number satisfying the given condition:",total_num)
