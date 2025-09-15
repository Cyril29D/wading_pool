# Task 1.5
# Prompt the user for an integer:
# ✓ if it's 42, display ”a” ;
# ✓ if it's smaller or equal than 21, display ”b” ;
# ✓ if it's even, display ”c” ;
# ✓ if this integer divided by 2 is smaller than 21 (excluded), display ”d” ;
# ✓ finally, if it's is odd and greater or equal than 45, display ”e” ;
# ✓ in any other cases, display ”f”.


nb = int(input())


if nb == 42:
    print("a")
elif nb <= 21:
    print("b")
elif nb % 2 == 0:
    print("c")
elif nb / 2 < 21:
    print("d")
elif nb % 2 == 1 and nb >= 45:
    print("e")
else:
    print("f")
