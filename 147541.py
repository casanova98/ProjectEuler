file = open("lala.txt", "r")
s = 0
lines = file.readlines()
for line in lines:
    s += int(line)
print(str(s)[:10])
    
