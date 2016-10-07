n=100
a=[1]*n
for i in range(2,100):
 if a[i]:
  for j in range(i*i,n,i):a[j]=0
print [i for i in range(len(a))if a[i]==1][2:]
