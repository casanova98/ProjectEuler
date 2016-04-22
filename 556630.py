array = []
for i in range(1, 1000):
    if i % 3 == 0:
        array.append(i)
    elif i % 5 == 0:
        array.append(i)
print(array)
sum = 0
for i in array:
    sum += i
print(sum)

    
        
