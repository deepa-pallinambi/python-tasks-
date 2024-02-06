with open("newfile2.txt","r") as file1:
    words=0
    c=list()
    for i in file1:
               i=i.replace(","," ")
               i=i.replace(".", " ")
               i=i.replace("'"," ")
               d=i.strip().split()
               for k in d:
                   if k not  in c:
                         c.append(k)
               for word in c:
                   words+=1
c.sort()
print(c,"there is :",words,"total unique words")



