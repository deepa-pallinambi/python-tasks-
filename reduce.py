import functools
c=print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5]))
d=print(functools.reduce(lambda x,y:x*y,[1,2,3,4,5]))
e=print(functools.reduce(lambda x,y:max(x,y),[1,2,3,4,5]))



