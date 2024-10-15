import random

name = input("type your name:- ")

print("Good Luck ! ", name)

words = ['food', 'sleep', 'car', 'manchurian',
         'python', 'samosa', 'food', 'makeup',
         'reverse', 'water', 'sun', 'moon' ,'gun','startup','absorb','abuse','accept','account']

word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win the game")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("wrong answer")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose !!! word was:- ",word)
