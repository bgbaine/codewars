def delete_nth(order, max_e):
    new = []
    for number in order:
        if new.count(number) < max_e:
            new.append(number)
    return new
