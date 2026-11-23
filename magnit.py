def group():
    n = int(input())
    group = 1
    prev = input()
    for i in range(n-1):
        curr = input()
        if curr != prev:
            group += 1
            prev = curr
    print(group)

def main():
    group()

if __name__ == "__main__":
    main()