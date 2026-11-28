def register(n):
    name = {}
    res = []
    for _ in range(n):
        s = input()
        if s not in name:
            name[s] = 1
            res.append("OK")
        else:
            res.append(f"{s}{name[s]}")
            name[s] += 1
            
    return res
def main():
    n = int(input())
    res = register(n)
    print("\n".join(res))

if __name__ == "__main__":
    main()

