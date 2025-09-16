# Write a generic function to checks passwords : they must contain more than 16 characters, at least 3
# special character and 1 number.
# This function should be callable the following way:
# passcheck (fun1 , 16 , " mysecretpassword ")
# passcheck (fun2 , 3 , " mysecretpassword ")
# passcheck (fun3 , 1 , " mysecretpassword ")

import re


def funA(s, n):
    return len(s) >= n


def funB(s, n):
    speciaux = re.findall(r"[@_!#$%^&*()<>?/\|}{~:]", s)
    return len(speciaux) >= n


def funC(s, n):
    nombre = re.findall(r"[0123456789]", s)
    return len(nombre) >= n


def passcheck(mdp):
    if funA(mdp, 16) and funC(mdp, 1) and funB(mdp, 3):
        print("mot de passe validé")
    else:
        print("16 characters,3 special character ,  1 number")
        return


passcheck("fgdggfbgfgrhf1***")
