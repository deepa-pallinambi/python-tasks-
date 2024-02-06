def lis(*n):
    c=[]
    for i in n:
        v=["a","e","i","o","u"]
        for m in list(i):
            for k in list(v):
                if m==k:
                   i=i.replace(k," ")
        c+=[i]
    print(c)




lis("hi","hello","welcome")
