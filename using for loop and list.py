#program 4 anudip foundation
#Implementing list(collection datatype) through example of sum and average
suming = 0  # sum and average variables are initialized to 0 otherwise it holds garbage value which may effect our result
average = 0
n=0  # n is used to count number of elements
print("elements are:")
for x in [80,90 , 30 , 20 , 70 , 80 , 39 , 87]: #for loop is used when number of iterations are known
    suming = suming+x  # for each itertion value is added
    n= n+1
average = suming/n
print("total elements in the list  :" ,n)
print("sum of given elements : ", suming)
print("average of given elements : ", average)
