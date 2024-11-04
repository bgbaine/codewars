def digital_root(n) -> int:
    n_str = str(n)
    return n if len(n_str) == 1 else digital_root(sum(map(int, n_str)))
