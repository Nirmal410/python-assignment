z=int(input("size:"))
a=[]
for j in range(z):
    n=int(input("elements:"))
    a.append(n)
print(a)
for i in a:
    if i>0:
        print(i,end=" ")
