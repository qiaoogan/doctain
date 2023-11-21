import os

count = 0
with open("testfile.txt","r") as f:
    txt = f.read()
    count = txt.count("read_item")
    print(f'main.py include read_item : {count}')
with open("../main.py","a") as f:
    f.write(txt.replace("read_item","read_item1"))

print(f.closed)

os.remove("testfile.txt")







