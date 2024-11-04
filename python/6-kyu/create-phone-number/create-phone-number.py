def create_phone_number(n):
    n = list(map(str, n))
    phone_number = ""
    for i in range(10):
        match i:
            case 0:
                phone_number += f"({n[i]}"
            case 2:
                phone_number += f"{n[i]}) "
            case 5:
                phone_number += f"{n[i]}-"
            case _:
                phone_number += f"{n[i]}"
    return phone_number
