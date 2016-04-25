def fibo():
    array = [1, 2]
    while array[-1] <= 4000000:
        array.append(array[-1]+array[-2])
    array.remove(array[-1])
    total = 0
    for i in array:
        if i % 2 == 0:
            total += i
    print(total)
            
