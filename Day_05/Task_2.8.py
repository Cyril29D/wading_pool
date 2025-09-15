# Test this code and try to explain it:
first_names = [" Jackie ", " Chuck ", " Arnold ", " Sylvester "]
last_names = [" Stallone ", " Schwarzenegger ", " Norris ", " Chan "]
magic = [*zip(first_names, last_names[::-1])]
# "zip" associe les éléments des deux listes puis "[::-1] inverse la liste "last_names"
print(magic[0])
print(magic[3])
print(magic[1][0])
print(magic[0][1])
print(magic[2])
