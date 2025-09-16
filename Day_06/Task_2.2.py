# Write a recursive function that prompt the user for a string of characters,
# strip out the spaces and punctuation signs, lowercase the string, then test if is a palindrome.

import re
import string

# .strip() pour supprimer les espaces
# s = "string. With. Punctuations!?"
# out = s.translate(str.maketrans("", "", string.punctuation)) permet de supprimer les ponctuations
# .replace(" ", "").replace(",", "").replace(".", "")


def palindrome(p=""):
    p = p.lower().replace(" ", "").replace(",", "").replace(".", "")
    if len(p) == 0:
        return True
    if p[0] == p[-1]:

        return palindrome(p[1:-1])

    else:
        return False


print(palindrome(input()))
