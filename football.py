def football(n):
    i = 1
    counter = 1
    while i < len(n):
        if n[i] == n[i-1]:
            counter += 1
            if counter >= 7:
                return "YES"
                        
        else:
            counter = 1
        i += 1
      
    return "NO"

def main():
    a = input()
    print(football(a))

if __name__ == "__main__":
    main()