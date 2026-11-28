def steps(n,s):
    current = 1
    max1 = 1
    i = 1
    while i < n:
        if s[i] >=s[i-1]:
            current += 1
            max1 = max(max1, current)
        else:
            current = 1
        i += 1
    return max1
def main():
    n = int(input())
    s = list(map(int, input().split()))
    print(steps(n,s))

if __name__ == "__main__":
    main()