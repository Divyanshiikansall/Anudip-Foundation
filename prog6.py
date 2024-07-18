#program 6 anudip foundation

suming = 0
average = 0
n=0
print("elements are:")
for x in [80,90 , 30 , 20 , 70 , 80 , 39 , 87]:
    suming = suming+x
    n= n+1
    print(x)
average = suming/n
print("total elements in the list  :" ,n)
print("sum of given elements : ", suming)
print("average of given elements : ", average)
