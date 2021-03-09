# binary.2.py
n = 39
remainders = []
while n > 0:
    # remainder = n % 2
    # remainders.append(remainder)
    # n //= 2
    n, remainder = divmod(n, 2)
    remainders.append(remainder)
    # remainders.insert(0, remainder) # book does this, not sure why??

print(remainders)


resulto = 0
for power, num in enumerate(remainders):
    resulto += num * 2 ** power

print(resulto)