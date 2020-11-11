def minionGame(string):
    a = 0
    b = 0
    vowels = "AEIOU"

    for i in range(len(string)):
        if string[i] in vowels:
            a += (len(string) - i)
        else:
            b += (len(string) - i)

    if a > b:
        print("Kevin {}".fromat(a))
    elif b > a:
        print("Stuart {}".format(b))
    else:
        print("Draw")

if __name__ == "__main__":
    # Here you have to compare scores
    s = input()
    minionGame(s)
