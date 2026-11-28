def dragon(k, l, m, n , d):
    for i in range(1, d + 1):
        if i % k != 0 and i % l != 0 and i % m != 0 and i % n != 0:
            d -= 1
    return d
def main():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    print(dragon(k, l, m, n, d))

if __name__ == "__main__":
    main()