def sorting(n):
    return n.sort()

def main():
    x = int(input())
    n = list(map(int, input().split()))
    sorting(n)
    print(*n)
if __name__ == "__main__":
    main()
