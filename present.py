def present():
    n = int(input())
    per = list(map(int, input().split()))
    ans = [0] * n
    i=0
    giver = 0
    for i in range(n):
        giver = i +1
        reciver = per[i]
        ans[reciver-1] = giver
    print(*ans)
def main():
    present()
if __name__ == "__main__":
    main()