def f(n):

    if n % 2 == 0:
        print(n // 2)
    else:
        print(-(n + 1) // 2)

def main():
    n = int(input())
    f(n)

if __name__ == "__main__":
    main()