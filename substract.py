def subber(n, k):
    i =0
    while i != k:
        i += 1
        if n %10 ==0:
            n = n /10
        else:
            n= n - 1
    return int(n)

def main():
    a, b = map(int, input().split())

    print(subber(a, b))

if __name__ == "__main__":
    main()