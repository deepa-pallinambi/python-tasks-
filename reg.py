import re
text="DOB of  arun is 05/12/2000 \n and DOB of varun is 05/12/2000 \n and DOB of rohit is 05/12/2000"
x=re.search("05/12/2000",text)
print(x.start())