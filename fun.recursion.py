def sumof(a,s):
    if s==0:
        return 0
    else:
        return a[s-1]+ sumof(a,s-1)
n=int(input("enter the number of elements for the list:"))
b=[]
for i in range(0,n):
    element=int(input("enter element:"))
    b.append(element)
d=sumof(b,n)
print ("sum of items in the list is,",d)




