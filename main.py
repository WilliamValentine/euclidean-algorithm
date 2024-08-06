def euclidean_algorithm(a, b):
    if a == 0 or b == 0:
        quit("Both inputs must not be equal 0")
    r = -1
    while r != 0:
        if a > b:
            r = a % b  # Remainder
            a = b
        else:
            r = b % a
        b = r
    return a


x = int(input("Enter a: "))
y = int(input("Enter b: "))

gcd = euclidean_algorithm(x, y)
print("The GCD of", x, "and", y, "is", gcd)
