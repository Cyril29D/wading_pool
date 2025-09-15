# Write a program that takes an integer n as input. Then, for each integer from 2 to n/2, display the list of its
# multiples strictly smaller than n, in descending order.

nb = 14

for i in range(2, nb // 2 + 1):
    for p in reversed(range(nb)):
        if p % i == 0 and p != 0:
            print(p, end=" ")
    print("")
