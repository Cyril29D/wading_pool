# Test this code and try to explain it:
# si l'élément de la liste est pair alors il prend la division entière par 2 ou sinon si c'est impair alors il le multiplie par 2

liste = [x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]]
print(liste)
