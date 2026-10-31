from getters import get_current_datetime

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
    string_3 = "String for master branch commit"
    print(f"Начинаем работу в {get_current_datetime()}")
    print_abc()
    print(factorial(5))
    print(diff(5, 2))