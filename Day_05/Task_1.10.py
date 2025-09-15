# Task 1.10
# Add the ten integers from 11 to 21 at the end of your list.
# Please, do not do it in 10 similar lines. Be smart and lazy.

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
addition = 10

for i in range(11):
    addition += 1
    print(addition)
    liste.append(addition)
print(liste)
