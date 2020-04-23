def prime_factors(n):
    if n <= 0 :
        n = -n
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

def sum_for_list(lst):
    all_prime = []
    for i in lst:
        temp = prime_factors(i)
        all_prime += temp
    all_prime = sorted(set(all_prime))
    res = []
    for prime in all_prime:
        res.append([prime, sum([i for i in lst if i % prime == 0])])
    return res
