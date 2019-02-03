names = []
names_count = int(input("How many names are you going to enter?: "))

for x in range(names_count):
    if len(names) < names_count:
        names.append(input("Please enter a name: "))


#print(names)
print("%30s" % ("#" * 30))
print("The names you've entered are: ")
print(*names, sep='\n')

#доста грозен код :D
