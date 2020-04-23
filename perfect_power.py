import operator
from collections import Counter
from functools import reduce
from fractions import gcd

def isPP(n):
    factorlist = prime_factors(n)
    counter = Counter(factorlist)
    gcd_number = reduce(gcd, counter.values())
    factorset = set(factorlist)
    if gcd_number > 1:

        return [ reduce(operator.mul, [ i ** (factorlist.count(i) // gcd_number)  for i in factorset]) , gcd_number]
    return None
    
def prime_factors(n):
    f, res = 3, []
    # if is_prime(n):
    #     return [n]
    while n % 2 == 0:
        res.append(2)
        n //= 2

    while f * f <= n:
        while n % f == 0:
            res.append(f)
            n //= f
        f += 2
    if n > 1:
        res.append(n)
    res.sort()
    return res
