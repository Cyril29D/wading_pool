# First brick
# Write a function that takes an integer as parameter and prints ”You loose!” if the parameter is greater or
# equal than 12.
import random
import string
from english_words import get_english_words_set

web2lowerset = get_english_words_set(["web2"], lower=True)


def penalty(nb):
    return nb >= 12


def win(add):
    return add < 12


def random_word():
    words = ["pitaya", "francais", "paris", "espagne", "package", "inspiration"]
    return random.choice(words)


def find_letter(mot, lettre_trouvee):
    affiche = ""
    for lettre in mot:
        if lettre in lettre_trouvee:
            affiche += lettre
        else:
            affiche += "_"
    return affiche


def game():
    mot = random_word().upper()
    lettres_trouvees = []
    penalties = 0
    while not penalty(penalties):
        guess = input().upper()

        if len(guess) == 1:
            if guess in mot:
                lettres_trouvees.append(guess)
                print(f"Found one '{guess}'")
            else:
                penalties += 1
                print(f"'{guess}' not found")
        else:
            if guess == mot:
                print(f"{mot}: correct guess - {penalties} penalties")
                return
            else:
                penalties += 6
                print(f"{guess}: incorrect guess")

        affichage = find_letter(mot, lettres_trouvees).upper()
        print(" ".join(affichage) + f" / {penalties} penalties")
        if "_" not in affichage:
            print(f"{mot}: correct guess - {penalties} penalties")
            return
    print(f"The word was {mot}")


game()
