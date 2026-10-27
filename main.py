
def print_abc():
    print("abc")


def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


def diff(n, m):
    return n - m


if __name__ == "__main__":
    print_abc()
    print(factorial(5))
    print(diff(5, 2))