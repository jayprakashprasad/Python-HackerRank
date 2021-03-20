if __name__ == '__main__':
    n = int(input(4))

    arr = list(map(int, input().rstrip().split()))
    print(" ".join(map(str, arr[::-1])))
    
    #2nd way
    n = int(input(4))
    arr = list(int,input(1,4,3,2))
    print(" ".join(str, arr[::-1]))

