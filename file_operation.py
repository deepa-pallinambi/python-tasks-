def filehandling():
    print("""reading files can only be performed in existing files \n \n where as a new file will be created if there is no file existing if and only if \n\nthe file opened with writing mode\n""")
def read():
    print("to read a Text File")
    with open('file_name.txt','r') as f1:
        print(f1.read())
def write():
    print("to write on to a Text File")
    with open ('file_name.txt','w') as f2:
        print(f2.writelines("hello"))
