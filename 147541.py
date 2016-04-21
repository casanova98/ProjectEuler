file = open("lala.txt", "r")
s = 0
lines = file.readlines()
for line in lines:
    print("OL")
    s += int(line)
print(str(s)[:10])
    
