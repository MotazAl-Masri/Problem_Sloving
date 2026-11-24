def binary():
    a = input()
    b = input()
    res = bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a))
    print(res)

def main():
    binary()

if __name__ == "__main__":
    main()