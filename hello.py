def hello():
    a = input()
    target = "hello"
    j = 0
    for char in a:
        if char == target[j]:
            j += 1
            if j == 5:
                return "YES"
    return "NO"
def main():
    print(hello())

if __name__ == "__main__":
    main()