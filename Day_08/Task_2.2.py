import turtle

toto = turtle.Screen()
# toto est l'écran du turtle
toto.bgcolor("black")
# on change le fond d'ecran en noir
titi = turtle.Turtle()
# titi est le curseur
titi.color("red")
# on change le curceur en rouge
for i in range(3):
    titi.right(90)
    titi.circle(42)
toto.exitonclick()
