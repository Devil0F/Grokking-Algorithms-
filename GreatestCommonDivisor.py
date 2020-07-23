def GreatestCommonDivisor(x,y):
    if x % y == 0:
        return y
    return GreatestCommonDivisor(y,x%y)

print(GreatestCommonDivisor(1680,640))
