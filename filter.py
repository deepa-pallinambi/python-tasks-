a=list("abghejikohj")
def vowel(x):
    v=('a','e','i','o','u')
    return x in v
b=list(filter(vowel,a))
print("vowels :",b)
def prime(x):
    if x==0 or x==1:
        check="is not"
    elif x==2:
        return(x)
    elif x>1:
        for i in range(2,x):
            if x%i==0:
                break
            else:
                continue
        if x%i!=0:
            return(x)


b=print(list(filter(prime,[2,3,4,5,6,7,8,9,11,12,15,20,25,23,27,29])))







