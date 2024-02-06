with open("newfile2.txt","r") as file1:
    c=0
    for i in file1.read():
        if i=="h":
            c+=1
    print("ocuurances of the word ,h is:",c)