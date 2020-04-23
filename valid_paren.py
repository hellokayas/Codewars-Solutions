def valid_parentheses(string):
    #stack = []
    ct = 0
    f = 0
    if len(string) == 0:
        return True
    for i in string:
        if i == "(":
            #stack.append("(")
            ct += 1
        if i == ")":
            if ct == 0:
                f = 1
                break
            else:
                #stack.pop()
                ct -= 1
    if f == 1:
        return False
    if ct == 0:
        return True
    else:
        return False #your code here
