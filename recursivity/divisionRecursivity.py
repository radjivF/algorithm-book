def divide(x, y):
    if x == 0: return (0, 0)
    quotient, rest = divide(x/2, y)
    quotient *= 2
    rest *= 2
    if x % 2 == 1:
        rest += 1
    if rest >= y:
        rest -= y
        quotient += 1
    print "quotient ", quotient,"rest ", rest
    return (quotient, rest)

assert divide(4, 2) == (2, 0)
assert divide(54, 3) == (5, 2)
assert divide(34, 15) == (0, 10)
assert divide(6, 2) == (2, 4)
