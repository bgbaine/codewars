def narcissistic(value) -> bool:
    value_str: str = str(value)
    return sum([int(digit) ** len(value_str) for digit in value_str]) == value
