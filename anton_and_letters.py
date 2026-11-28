def setting(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = set()
    for letter in s:
        if letter in alphabet:
            res.add(letter)
    return len(res)
def main():
    s = input()
    print(setting(s))
if __name__ == "__main__":
    main()