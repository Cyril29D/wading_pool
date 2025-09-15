# Task 3.4 Write a program that:
# -ask the user to type a string ;
# -extracts the first letter of each word in the string ;
# -join these letters to make a word.


phrase = input("entrez une chaine de caractère :")
liste_mots = phrase.split()

print(liste_mots)
result = ""
for mot in liste_mots:
    result += mot[0]

print(result)
