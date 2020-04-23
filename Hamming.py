def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n//2 + 1, 2):
        if n % i == 0:
            return False
        return True

# print([i for i in range(6, 100) if is_prime(i)])
# import pdb; pdb.set_trace()  # breakpoint 5bd6f467 //



def hamming(n):
    factors = [2, 3, 5]
    elements = [1 for i in range(n)]
    nextIndex = [0 for i in range(len(factors)) ]
    nextFrom = factors[::]#[0 for i in range(len(generator)) ]
    for i in range(1, n):
        nextNumber = 2**64
        for j in nextFrom:
            if j < nextNumber:
                nextNumber = j
        elements[i] = nextNumber
        for j in range(len(factors)):
            if nextFrom[j] == nextNumber:
                nextIndex[j] += 1
                nextFrom[j] = elements[nextIndex[j]] * factors[j]
        # print(elements)
    return elements[-1]
