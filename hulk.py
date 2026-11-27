def printing(n):
    s = []
    for i in range(1, n + 1):
        if i %2 !=0:
            s.append("I hate")
        else:
            s.append("I love")
    res = " that ".join(s) + " it"
    print(res)

def main():
    n = int(input())
    printing(n)

if __name__ == "__main__":
    main()