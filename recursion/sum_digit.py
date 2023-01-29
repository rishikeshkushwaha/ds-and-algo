

def sumDigits(n):
    if n in range(10):
        return n

    return n%10 + sumDigits(n//10)

print(sumDigits(5565))