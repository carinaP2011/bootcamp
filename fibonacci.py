n = 5 # int(input("Fibonacci Sequence!!!! \n How many numbers?"))
list1 = [1] if n > 0 else []
for x in range(n-1):
    list1.append(list1[x]+list1[-1])

return list1
