def get_pins(observed):
    from itertools import product
    dictx = {'1': ['1', '2', '4'], '2': ['1', '2', '3', '5'], '3': ['2', '3', '6'], '4': ['1', '4', '5', '7'], '5': ['2', '4', '5', '6', '8'],
             '6': ['3', '5', '6', '9'], '7': ['4', '7', '8'],
             '8': ['0', '5', '7', '8', '9'], '9': ['6', '8', '9'],
             '0': ['0', '8']
             }
    res = []
    if len(observed) == 1:
        res = dictx[observed]
        return res
    else:
        res = dictx[observed[0]]
        return [''.join(element) for element in set(product(res, get_pins(observed[1:])))]


print(get_pins('8'))
print(get_pins('11'))
print(get_pins('369'))


from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157',
             '52468', '6359', '748', '85790', '968')


def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
