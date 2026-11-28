def summer(n):
    res = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        if a + b == c or a + c == b or b + c == a:
            res.append("YES")
        else:
            res.append("NO")
    return res

def main():
    n = int(input())
    res = summer(n)
    print("\n".join(res))

if __name__ == "__main__":
    main()