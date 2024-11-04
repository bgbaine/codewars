def add_binary(a, b):
    sum = a + b
    sum_b = 0
    i = 1
    while sum > 0:
        sum_b += (sum % 2) * i
        sum = sum // 2
        i = i * 10
    return str(sum_b)
