from math import pi
def iter_pi(epsilon):
    appro = 0
    odd = 1
    sign = 1
    number_of_iterations = 0
    while abs(appro * 4 - pi) > epsilon:
        number_of_iterations += 1
        appro +=  1.0/(odd * sign)
        odd += 2
        sign *= -1
        #print appro
    return [number_of_iterations, round(appro*4, 10)]
