def gcd(a, b):
    assert int(a) == a and int(b) == b, 'numbers should be positive'
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(18, -38))
