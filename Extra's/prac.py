x = int(input())
y = int(input())
a = bin(x)
b = oct(y)
p = a[2:]
q = b[2:]
print("{},{}".format(p,q))
