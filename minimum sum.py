list1=input().split()
minsum=min(int(num1)+int(num2) for num1,num2 in zip(list1,list1[1:]))
print(minsum)

# zip function is used to take 2 binded values in a single iterate
# when loop starts firstly num1 stores first element of list1
# and takes 2nd element as num2
# second time num1 is 2nd element of list1 and num2 is third element of list1