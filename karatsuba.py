from math import floor, ceil


def karatsuba(x, y):
  sx = str(x)
  sy = str(y)
  n = max(len(sx), len(sy))
  if len(sx) == 1 and len(sy) == 1:
    return x*y
  m = ceil(n/2)
  a = int(x // (10**m))
  b = int(x % (10**m))
  c = int(y // (10**m))
  d = int(y % (10**m))
  ac = karatsuba(int(a), int(c))
  bd = karatsuba(int(b), int(d))
  adbc = karatsuba(int(a) + int(b), int(c) + int(d)) - ac - bd
  return int(str(ac) + '0' * 2 * m) + int(str(adbc) + '0' * m) + bd


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
