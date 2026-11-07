import math as mt
a,b,c = map(int, input().split())
x = int(mt.ceil(a/c))
y = int(mt.ceil(b/c))
print(x*y)