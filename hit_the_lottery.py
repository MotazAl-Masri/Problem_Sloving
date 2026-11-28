def bill(n):
    bills = [100, 20, 10, 5, 1]
    count = 0
    for b in bills:
        count += n // b
        n = n % b
    return count

def main():
    n = int(input())
    print(bill(n))

if __name__ == "__main__":
    main()