import random
import sys

FILE_NAME = 'answer.txt'

def myRandom() -> None:
    real = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(0, 10):
        k = random.randint(0, 9)
        tmp = real[i]
        real[i] = real[k]
        real[k] = tmp
    f = open(FILE_NAME, 'w')
    f.write('{:s}{:s}{:s}{:s}'.format(real[0], real[1], real[2], real[3]))
    f.close()

def myGuess(guess) -> None:
    counterA = 0
    counterB = 0
    f = open(FILE_NAME, 'r')
    ans = f.read()
    realNum = list(ans)
    f.close()

    for i in range(0, 4):
        if realNum[i]==guess[i]:
            counterA+=1
        for j in range(0, 4):
            if realNum[i]==guess[j] and i!=j:
                counterB+=1
    print('{:s}{:s}{:s}{:s}   {:d}A{:d}B'.format(guess[0], guess[1], guess[2], guess[3], counterA, counterB))

    if counterA==4:
        print('You win!')
        sys.exit(0)
        return

def main() -> None:
    myRandom()
    while True:
        guess = input('Guess number: ')
        guessList = list(guess)
        myGuess(guessList)

if __name__=='__main__':
    main()
















