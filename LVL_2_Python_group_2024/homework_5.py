# 1
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


a = 1071
b = 462
result = gcd(a, b)
print(f"Найбільший спільний дільник чисел {a} і {b} = {result}")

# 2
def gcd_custom(a, b):
    if a == 0 or b == 0:
        return [a, b]

    if a >= 2 * b:
        return gcd_custom(a - 2 * b, b)

    if b >= 2 * a:
        return gcd_custom(a, b - 2 * a)
        return [a, b]

a = 22
b = 6
result = gcd_custom(a, b)
print(result)





