import random
import time
import sys
from time import sleep

passcode = []
# worddoor definitions
masterlist = {"volatile": "Adj. Unpredictable", "singularity": "Noun. Undefined", "obscure": "Adj. Uncertain",
              "oblivion": "Noun. Unaware"}
answerlist = ["volatile", "singularity", "obscure", "oblivion"]
line_1 = "\n>>> You are detained underground. You are about to die from starvation and dehydration."
line_2 = "\nYou must pass a series of tests to survive."
line_3 = "\nIf you pass the first test, you obtain a code for a week's worth of water."
line_4 = "\nIf you pass the second test, you obtain a code for week's worth of food and water."
line_5 = "\nIf you pass both tests, you will get a bypass code to leave the premises. You only get one shot, make it count. \n"


def intro():
    for x in line_1:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.01)
    sleep(1)
    for x in line_2:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.01)
    sleep(1)
    for x in line_3:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.01)
    sleep(1)
    for x in line_4:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.01)
    sleep(1)
    for x in line_5:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.01)
    sleep(2)


def worddoorprep():
    random.shuffle(answerlist)
    global answer
    answer = list(answerlist[0])
    global display
    display = []
    display.extend(answer)


def worddoor():
    global confirmation
    confirmation = 0
    for h in range(len(display)):
        display[h] = "_"

    if 'volatile' in answerlist[0]:
        print(masterlist[list(masterlist)[0]])
    elif 'singularity' in answerlist[0]:
        print(masterlist[list(masterlist)[1]])
    elif 'obscure' in answerlist[0]:
        print(masterlist[list(masterlist)[2]])
    elif 'oblivion' in answerlist[0]:
        print(masterlist[list(masterlist)[3]])

    print(' '.join(display))
    print()
    wordguesses = 20
    count = len(answer)
    while count > (0) and wordguesses != (0):
        if count > (0):
            print("You have ", wordguesses, " guesses left. ")
            guess = input("\nPlease guess a letter: ")
            wordguesses = wordguesses - 1
            guess = guess.lower()
            for h in range(len(answer)):
                if display[h] == guess:
                    print("\nYou already guessed that! \n")
                elif answer[h] == guess:
                    display[h] = guess
                    count = count - 1
                    confirmation = confirmation + 1
            print(' '.join(display))
        if wordguesses == 0:
            print("\nYou didn't get the word in time! The answer was: ", answerlist[0])
            confirmation = 0


# numdoor definitions
def even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def countEven(password):
    numeven = 0
    for x in password:
        if even(int(x)):
            numeven += 1
    return numeven


def Sum(password):
    _sum_ = 0
    for x in password:
        _sum_ += int(x)
    return _sum_


def product(password):
    _product_ = 1
    for x in password:
        _product_ *= int(x)
    return _product_


def numdoor():
    integer = random.randint(4, 5)
    chars = "1234567890"
    passnum = random.sample(chars, integer)
    lives = (integer) * 2
    _sum_ = Sum(passnum)
    print('loading...')
    time.sleep(random.randint(0, 3))
    passnum = ''.join(passnum)
    print("\nCODE GENERATED")
    print('\nClues: ')
    print('The code is', integer, 'numbers long')
    print('Its sum is', _sum_)
    _product_ = product(passnum)
    print('Its product is', _product_)
    numeven = countEven(passnum)
    print('The number of even numbers is', numeven)
    numodd = integer - numeven
    print('The number of odd numbers is', numodd)
    print('Its first number is', int(passnum[0]))
    print('Its last number is', int(passnum[-1]))
    print('Its highest number is', str(max(passnum)))
    print('Its lowest number is', str(min(passnum)))
    print('\nYou have', lives, 'tries left')
    # checking
    global conf
    conf = 0
    while lives > 0:
        numan = input('What is the code? ')
        if numan == passnum:
            passcode.extend(list(numan))
            print("\nYou guessed the number correctly! You have now unlocked: \n", passcode)
            conf = conf + 1
            break
        if numan != passnum:
            lives -= 1
            print('you have', lives, 'tries left')
            print('That was not correct')
            if lives <= 0:
                print("You didn't crack the code. It was", passnum)
                break


# main
intro()
input("\nPress Enter to proceed: ")
print('\nloading...')
time.sleep(random.randint(0, 3))
print(
    "\nYou have arrived at the first door. To pass this door you must correctly guess all the letters in the word in 20 tries or less. Here is your word: \n")
sleep(2)
worddoorprep()
worddoor()
if confirmation == len(answer):
    passcode.extend(answer)
    print("\nYou guessed the word correctly! These letters are now unlocked: \n", passcode)
input("\nPress Enter to proceed to the next door: ")
print(
    "\nYou have arrived at the second door. To pass this door you must correctly guess all the numbers in the code correctly: \n")
numdoor()
input("\nPress Enter to proceed to the next door: ")
print("\nYou have arrived at the last door. Let's take a look: \n")
sleep(2)
if conf == 1 and confirmation == len(answer):
    print("You passed both tests! You can now generate a code using: \n", passcode)
    sleep(2)
    input("Press Enter to generate your new password!")
    random.shuffle(passcode)
    print("Your Password: ", ''.join(passcode), "\nYou are free!")
elif conf == 1 and confirmation != len(answer):
    print("You only passed the second test! You can only generate a code using: \n", passcode)
    sleep(2)
    input("Press Enter to generate your new password!")
    random.shuffle(passcode)
    print("Your Password: ", ''.join(passcode),
          "\nYou now have enough food and water for a week. Keep looking for other means of escape. Good luck!")
elif conf != 1 and confirmation == len(answer):
    print("You only passed the first test! You can only generate a code using: \n", passcode)
    sleep(2)
    input("Press Enter to generate your new password!")
    random.shuffle(passcode)
    print("Your Password: ", ''.join(passcode),
          "\nYou now have enough water for a week. Keep looking for other means of escape. Good luck!")
else:
    print(
        "You didn't pass any of the tests. Out of pity we will provide you with the standard passcode, \n[EndMyMissouri] \nto give you enough food and water to live another day. We wish you the best of luck.")