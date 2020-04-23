from functools import reduce


def last_digit(numbers):
    
    def get_exp(n):
        
        if n <= 4:
            return n
        
        if n % 100 > 1:
            end = n % 100
        else:
            end = n % 1000

        if end % 4 == 0:
            exp = 4
        else:
            exp = end % 4

        if exp > 1:
            ans = exp
        else:
            ans = end
        
        return ans
    
    if not numbers:
        return 1
    elif len(numbers) == 1:
        return numbers[0] % 10
    elif len(numbers) == 2:
        expo = numbers[1]
    else:
        expo = reduce(lambda y, x: x ** get_exp(y), numbers[1:][::-1])
    
    return ((numbers[0] % 10) ** get_exp(expo)) % 10
