def decimal_binary(n):
    if n < 2:
        return n
    return n%2 + 10*decimal_binary(n // 2)

n = 10
print(decimal_binary(n))
print(bin(n)[2:])
