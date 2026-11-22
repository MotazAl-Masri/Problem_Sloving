def update_counter(counter, p, q):
    if q - p >= 2:
        counter += 1
    return counter

def george():
    n = int(input())

    counter = 0
    for i in range(n):
        p, q = map(int, input().split())
        counter = update_counter(counter, p, q)
    return counter


def main():
    print(george())

if __name__ == "__main__":
    main()