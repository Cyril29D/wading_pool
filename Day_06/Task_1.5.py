# Add a parameter to provide the possibility for veg sandwich (double vegetables + no ham).
# If this option isn't specified, the sandwich must be a lettuce-tomato-double ham one by default


def bread():
    print(" <////////// > ")


def lettuce():
    print(" ~~~~~~~~~~~~ ")


def tomato():
    print(" O O O O O O ")


def ham():
    print(" ============ ")


def commande(i, v):
    for i in range(i):
        bread(), lettuce(), tomato(), ham()
    for v in range(v):
        bread(), lettuce(), tomato()


commande(2, 3)
