def convert(input, source, target):
    if source == target or len(input) < 1:
        return input
    total = 0
    for idx, cher in enumerate(input):
        # print(cher, source.find(cher))
        total += len(source) ** (len(input)-1-idx) * source.find(cher)
    if total < len(target):
        return target[total]
    result = []
    # print(total)
    while total > 0:
        total, residual = divmod(total, len(target))
        result.append(target[residual])
    return ''.join(result[::-1])
