dict={"name":"john","age":25,"address":"newyork"}
print(type(dict))
print(dict)
dict["phone"]='1234567890'
print(dict)
dict.pop("address")
print(dict)
print(dict["age"])
if "phone" in dict.keys():
    print("available")
else:
    print("not available")