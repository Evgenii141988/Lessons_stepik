def get_body_mass_index(m: float, h: float) -> float:
    return round(m / h ** 2, 2)


if __name__ == '__main__':
    M = float(input())
    H = float(input())
    print(get_body_mass_index(M, H))
