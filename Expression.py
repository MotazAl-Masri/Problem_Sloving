def f1(a,b,c):
    return a+b+c
def f2(a,b,c):
    return a*b*c
def f3(a,b,c):
    return a*(b+c)
def f4(a,b,c):
    return (a+b)*c
def f5(a,b,c):
    return a+(b*c)
def f6(a,b,c):
    return (a*b)+c
def maximeze(a,b,c):
    return max(f1(a,b,c),f2(a,b,c),f3(a,b,c),f4(a,b,c),f5(a,b,c),f6(a,b,c))
def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(maximeze(a,b,c))
if __name__ == "__main__":
    main()