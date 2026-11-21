def queue(s,t,n):

    for i in range(t):
        s = s.replace("BG", "GB")
    return s

def main():
    n,t = map(int, input().split())
    s = input()
    print(queue(s,t,n))

if __name__ == "__main__":
    main()
    

