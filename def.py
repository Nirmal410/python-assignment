def z(arr,len):
    y={}
    for i in range(Len):
        if (arr[i] in y):
            y[arr[i]]=y[arr[i]]+1
        else:
            y[arr[i]]=1
    size=len(y)
    while (size>0):
        c=0
        a=0
        for key,value in y.items():
            if (value>c or (value==c and key>a)):
                a=key
                c=value
        print(f"{a}-{c}")
        y.pop(a)
        size-=1
str="geeksforgeeks"
Len=len(str)
z(list(str),len)
