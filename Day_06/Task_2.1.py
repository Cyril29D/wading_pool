# Write a recursive function that computes the sum of all integers from 1 to n, a given parameter


def recursive(r):
    if r > 0:
        result = r + recursive(r - 1)
        print(result)
    else:
        result = 0
    return result


recursive(42)
