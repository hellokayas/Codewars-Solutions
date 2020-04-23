def gcd (a,b):
    if (b == 0):
        return a
    else:
        return gcd (b, a % b)
def solution(a):
    if a == []:
        return None
    res = a[0]
    for c in a[1::]:
        res = gcd(res , c)
    return res*len(a)
