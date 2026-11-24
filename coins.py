def coin():
    n = int(input())
    coins = list(map(int, input().split()))
    coins.sort()
    coins.reverse()
    count = 0
    my_sum = 0
    for i in range(n):
        total = sum(coins)
        my_sum += coins[i]
        count += 1
        if my_sum > total - my_sum:
            
            break
    print(count)
def main():
    coin()

if __name__ == "__main__":
    main()