def f(x):
    if x==0 or x==1:
        return 1
    else:
        return x*f(x-1)

print(f(8))
print(f(5))
print(f(1))