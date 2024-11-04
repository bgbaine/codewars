def past(h, m, s):
    h *= pow(60, 2) * 1000
    m *= 60 * 1000
    s *= 1000
    return h + m + s
