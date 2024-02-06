current_number = 1
rows=4
stop=2
for i in range(rows):
    for j in range(1,stop):
        print(current_number,end=(" "))
        current_number+=1
    print(" ")
    stop+=1

