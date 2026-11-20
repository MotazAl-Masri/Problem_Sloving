def year():
    x = int(input())
    x +=1
    a = True
    while a:
        if len(set(str(x))) == 4:
            print(x)
            a = False
        else:
            x += 1
def main():
    year()

if __name__ == "__main__":
    main()