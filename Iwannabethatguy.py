def sets(a, b, n):
    set_a = set(a)
    set_b = set(b)
    s = set_a.union(set_b)
    return len(s) == n
def main():
    n = int(input())
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]
    if sets(a, b, n):
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
if __name__ == "__main__":
    main()