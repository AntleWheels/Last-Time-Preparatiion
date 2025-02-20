name = str(input("Enter the name :"))
name = name.lower()
for i in range(len(name)-1,-1,-1):
    print(name[i],end="")