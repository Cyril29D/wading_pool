# Write 3 functions, each taking a string s and an integer n as parameters and returning a boolean:
# ✓ funA checks if s contains at least n characters;
# ✓ funB checks if s contains at least n special characters;
# ✓ funC checks if s contains at least n numbers.
import re


def funA(s, n):
    return len(s) >= n


def funB(s, n):
    speciaux = re.findall(r"[@_!#$%^&*()<>?/\|}{~:]", s)
    return len(speciaux) >= n


def funC(s, n):
    nombre = re.findall(r"[0123456789]", s)
    return len(nombre) >= n


print(funA("azerty a", 13))

print(funB("Bonjouefbh!!=", 4))

print(funC("Bonjouer 2434", 4))
