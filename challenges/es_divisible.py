def es_divisible(n: int, d: int) -> int:
    if d > 0 and n % d == 0 :
        if n % (2 * d) == 0:
            return 2
        else:
            return 1
    else:
        return 0

print(es_divisible(5,2))

