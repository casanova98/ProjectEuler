def factors(n):
    num = n
    i = 2
    while i * i < num:
        while num % i == 0:
            num = num / i
        i += 1
    print(num)
