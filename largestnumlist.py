a =[]
n = int(input("Enter Number Of Elements"))
for i in range(1,n+1):
  b=int(input("Enter Element"))
  a.append(b)
a.sort(n)
print("Largest Element is",a[n-1])
      
