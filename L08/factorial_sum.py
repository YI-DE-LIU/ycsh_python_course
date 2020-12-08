#sum = 1
#a = 1
#n = int(input())
#for i in range(1,n+1):
 #   sum *= i
  #  print(sum)
   # a = a +sum
#print(a)

sum = 1
a = 1
i = 0
n = int(input())
while i < n:
    i += 1
    sum *= i
    a = a + sum
print(a)