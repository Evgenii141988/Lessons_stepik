def get_body_mass_index(m: float, h: float) -> float:
    return round(m / h ** 2, 2)


if __name__ == '__main__':
    weight = float(input())
    height = float(input())
    print(get_body_mass_index(weight, height))
