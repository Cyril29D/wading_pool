# Generate the lyrics of the song ”99 bottles of beer”.
# The songs ends when there is no more bottles on the wall.
# 1 bottle is singular...

beer = 0
for i in range(100):
    beer += 1
    print(str(beer) + "bottles of beer on the wall")
    print(str(beer) + "bottles of beer Take one down and pass it around")
