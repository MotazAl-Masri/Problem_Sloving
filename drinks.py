def drinks():
    n = int( input() )
    per = list( map( int, input().split() ) )
    print(sum(per) / n)
def main():
    drinks()
if __name__ == "__main__":
    main()