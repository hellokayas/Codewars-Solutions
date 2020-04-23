def disemvowel(string):
    L = ['a','e','o','i','u','A','E','I','O','U']
    s = ""
    for i in string:
        if i not in L:
            s = s + i
    return s
