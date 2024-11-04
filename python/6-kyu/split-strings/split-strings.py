def solution(s) -> list[str]:
    size = len(s)
    iterator = 2
    return [
        (
            s[i : i + iterator] + "_"
            if size % 2 == 1 and i == len(s) - 1
            else s[i : i + iterator]
        )
        for i in range(0, size, 2)
    ]
