# For all integers from -30 to 30:
# ✓ if it's a multiple of 3, display ”Fizz” ;
# ✓ if it's a multiple of 5, display ”Buzz” ;
# ✓ if it's a multiple of 3 and 5, display ”FizzBuzz” ;
# ✓ if it does not meet any of the previous conditions, just print the integer itself.


for i in range(-30, 31):
    if nb % 3 == 0:
        print("Fizz")
    elif nb % 5 == 0:
        print("Buzz")
    elif nb % 3 & 5 == 0:
        print("FizzBuzz")
    else:
        print(nb)
