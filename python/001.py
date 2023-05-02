str = input()
index = ""
for i in str:
    if i.islower():
        index += i.upper()
    else:
        index += i.lower()
print(index)