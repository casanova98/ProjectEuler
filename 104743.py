def prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**(0.5))+1):
        if n%i == 0:
            return False
count = 0
n = 1
while True:
    n += 1
    if prime(n) != False:
        count += 1
    if count == 10001:
        break
print(n)
