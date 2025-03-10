import random
import sys
from nltk.corpus import words


def clear_line():
    sys.stdout.write("\033[F")  # moving coursor upwards
    sys.stdout.write("\033[K")  # clearing line

word_list = words.words()
valid_words = [word.lower() for word in word_list if len(word) == 5]
password = random.choice(valid_words).lower()
mistakes = 0

while True:
    if mistakes == 6:
        print("Unfortunately tou lost. Try harder next time! The correct answer was")
        print(password)
    guess = input().lower()
    clear_line()
    if len(guess) != len(password):
        print("please type your guess in a correct length" )
        continue
    if guess not in valid_words:
        print("please make your guess an existing word")
        continue
    hint = ""
    counter = 0
    for i in range(len(guess)):
        if guess[i] == password[i]:
            hint += f"\033[32m{guess[i]}\033[0m"
            counter += 1
        elif guess[i] in password:
            hint += f"\033[33m{guess[i]}\033[0m"
        else:
            hint += f"\033[37m{guess[i]}\033[0m"
    print(hint)
    mistakes += 1
    if counter == len(password):
        print("Congratulations, Your guess is correct!")
        break
