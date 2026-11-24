def even_odds(n, a):
    odd_count = (n + 1) // 2
    
    if a <= odd_count:
        return 2 * a - 1
    else:
        return 2 * (a - odd_count)

def main():
    n, a = map(int, input().split())
    print(even_odds(n, a))

if __name__ == "__main__":
    main()