def fun(*n):
    a=[]
    for i in n:
        if len(i)>=5:
            print(i)
            a+=[i]
    print(a)

fun("hi","hello","welcome","123","12345","abcde","abc","thankyou","how are you")

