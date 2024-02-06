def gen(n):
    i=n.split()
    yield i
n="hi hello how are you welcome"
s=gen(n)
print(list(s))
def eve(n):
    for i in n:
        if i%2==0:
            yield i
n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
t=eve(n)
print(list(t))
def st(n):
    for i in n:
        b=list(i)
        if b[0]=="a":
            yield i
n=["hi","apple","abc","ant","welcome"]
c=st(n)
print(list(c))

