#!/usr/bin/env python
import math

def ct(m, n):
    return ((n*n + n) * (m*m + m)) / 4

diff = 1000000
bits = None

# don't know how to calculate the minimum of
# (n^2 + n)(m^2 + m) - 4000000 = 0

# know that 1, 2000 = 2001000, so we can assume
# upper bound is 2000
# alex suggested not doing the quadratic inline was cheating so
# here it is, assuming m = 1, we end up with
# (n^2+n)(1) - 4000000 = 0
quad = lambda a, b, c: (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
upper = int(quad(1, 1, -4000000))

for i in range(1, upper):
    for j in range(i, upper):
        x = ct(i, j)
        new_diff = abs(2000000 - x)
        if x + new_diff > 2000000 + diff:
            break
        if new_diff < diff:
            diff = new_diff
            bits = x, i, j, i*j 
print '%s...%s * %s = %s' % bits
