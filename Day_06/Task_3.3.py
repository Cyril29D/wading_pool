# Write a generic function to checks passwords : they must contain more than 16 characters, at least 3
# special character and 1 number.
# This function should be callable the following way:
import re


def funA(s, n):
    if len(s) >= n:
        return True
    else:
        return False


def funB(s, n):
    if len(re.findall(r"[@_!#$%^&*()<>?/\|}{~:]", s)) >= n:
        return True
    else:
        return False


def funC(s, n):
    if len(re.findall(r"[0123456789]", s)) >= n:
        return True
    else:
        return False


def passcheck(mdp):
    if funA(mdp, 16) and funC(mdp, 1) and funB(mdp, 3):
        print("mot de passe validé")
    else:
        print("16 characters,3 special character ,  1 number")
        return


passcheck("ééééééééééééééééééé1***")
