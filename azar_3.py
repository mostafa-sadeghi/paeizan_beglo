


import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(f'''This is Guess program and you can guess {NUM_DIGITS} digits number {MAX_GUESSES} times,
    Pico > correct digit but in wrong position.
    Fermi > correct digit and in right position.
    Bagels > No digit is correct
    ''')

    while True:
        secretNum = getSercretNum()
        print('secrect Num', secretNum)
        print('you have {}'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                if len(guess) > 0:
                    print('invalid input')
                guess = input('> ')
            numGuesses += 1
            verify = getVerify(guess, secretNum)
            print()
            print()
            print()
            print(verify)
            print()
            if guess == secretNum:
                break

        print('do you want play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thank you for playing!!!')


def getVerify(guess, secretNum):
    if guess == secretNum:
        return 'You got it!!'

    status = []
    for i in range(len(guess)):  # '145' '318'
        if guess[i] == secretNum[i]:
            status.append('Fermi')
        elif guess[i] in secretNum:
            status.append('Pico')
    if len(status) == 0:
        return 'Bagels'
    return status


def getSercretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    # string = ''.join(numbers[:NUM_DIGITS])
    # return string

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += numbers[i]
    return secretNum


main()
