import re

from math import ceil

def balance_statement(lst):
    stocks = re.split(r',\s+', lst)
    bad_formed = []
    pattern = re.compile(r'^([^\s]+)\s*(\d+)\s*(\d*\.\d+)\s*([BS])$')
    b_amount, s_amount = 0, 0
    for stock in stocks:
        if re.match(pattern, stock):
            
            match = re.match(pattern, stock)
            name, quant, price, bs = match.group(1), match.group(2), match.group(3), match.group(4)
            amount = int(quant) * float(price)
            if bs == 'B':
                b_amount += amount
            else:
                s_amount += amount
        elif not stock:
            continue
        else:
            bad_formed.append(stock)
    b_cnt=len(bad_formed)
    b_amount = int(round(b_amount, 0))
    s_amount = int(round(s_amount, 0))


    if b_cnt >0:
        bad = "; Badly formed {b_cnt}: {b_string} ;".format(b_cnt=b_cnt, b_string=' ;'.join(bad_formed))
    else:
        bad = ''
    return "Buy: {b} Sell: {s}{bad}".format(b=b_amount, s=s_amount, bad=bad )
