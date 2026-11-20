def problems():
    a = int(input())
    x = list(map(int,input().split()))
    for i in x:
        if i == 1:
            return "HARD"
            
    return "EASY"
        
def main():
    print(problems())

if __name__ == "__main__":
    main()