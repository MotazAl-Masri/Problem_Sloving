def panagrm(pangram):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(pangram.lower())
def main():
    n = int(input())
    panagram = input()
    if panagrm(panagram):
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()