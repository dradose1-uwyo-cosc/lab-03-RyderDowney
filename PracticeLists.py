names = ["Ryder", "McCoy", "Francesco", "Spencer", "RJ"]
print(names)
del names[0]
#or do names.remove("Ryder")
print(names)
#loop thought the names
#spencer is on my table
for name in names:
    print(f"{name} is on my table")
names.sort()
print(names)