#a=str(input("enter your name"))
#print(a[0],"**",a[-1])
l=["aba","1221","xyz","12","abcdea","mnm","oppo","malayalam","ll","12","121","123","12264678431"]
count=0
for i in list(l) :
    if len(i)>2 and i[0]==i[-1]:
        count+=1
print(count)


