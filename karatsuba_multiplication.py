import math


def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = int(math.ceil(float(n) / 2))

    # divide x into two half
    xh = int(math.floor(x / 10 ** m))
    xl = int(x % (10 ** m))

    # divide y into two half
    yh = int(math.floor(y / 10 ** m))
    yl = int(y % (10 ** m))

    # Karatsuba's algorithm.
    s1 = karatsuba(xh, yh)
    s2 = karatsuba(yl, xl)
    s3 = karatsuba(xh + xl, yh + yl)
    s4 = s3 - s2 - s1

    return int(s1 * (10 ** (m*2)) + s4 * (10 ** m) + s2)

a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627
print(f'{karatsuba(a,b):66.0f}')
print(8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184)
print(f'{karatsuba(1234,5678)}')  # 7006652
print(f'{karatsuba(1204,5678)}')  # 6836312
print(f'{karatsuba(123045,678912)}')
print(83536727040)
# print(f'{karatsuba(2,4411)}\n{2*4411}')
# print(f'{karatsuba(2211,4)}\n{2211*4}')
print(f'{a*b:66.0f}')
