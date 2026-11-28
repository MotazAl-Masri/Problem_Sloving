def general(n, soldier):
    max_index = 0
    min_index = 0

    for i in range(n):
        if soldier[i] > soldier[max_index]:
            max_index = i
        if soldier[i] <= soldier[min_index]:
            min_index = i

    if max_index > min_index:
        return max_index + (n - 1 - min_index) - 1
    else:
        return max_index + (n - 1 - min_index)

def main():
    n = int(input())
    soldier = list(map(int, input().split()))
    print(general(n, soldier))

if __name__ == "__main__":
    main()
