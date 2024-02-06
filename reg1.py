import re
text="""the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog again. 
the quick brown cat jumps over the lazy dog."""
x=re.findall("fox",text)
print(x)
y=re.findall("quick",text)
print(y)
z=re.findall(" c..",text)
print(z)
q=re.findall("t...lazy",text)
print(q)
r=re.match("the",text)
print(r.start())
s=re.search("fox",text)
print(s.start())
t=re.search("c",text)
print(t.start())
