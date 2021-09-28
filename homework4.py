def count_greater_or_equal(numbers, x):
    """
    Функия принимает на вход список чисел numbers и число x.
    Возращает количество элементов списка numbers больше либо равных x.
    """
    c = 0
    for number in numbers:
        if number >= x:
            c += 1
    return c


def test_count_greater_or_equal():
    assert count_greater_or_equal([1, 2, 3, 4, 5], 2) == 4
    assert count_greater_or_equal([1, 2, 3, 4, 5], 1) == 5
    assert count_greater_or_equal([1, 2, 3, 4, 5], 0) == 5
    assert count_greater_or_equal([0, 1], 2) == 0
    assert count_greater_or_equal([], 2) == 0
    print("Great your solution works!")

test_count_greater_or_equal()


def extend(a, b):
    """
    Даны два списка, надо их обеъединить и получить один список.
    Надо расширить список a элементами из списка b.
    """
    c = a + b
    return c


def test_extend():
    assert extend([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert extend([4, 5, 6], [1, 2, 3], ) == [4, 5, 6, 1, 2, 3]
    assert extend([], [4, 5, 6]) == [4, 5, 6]
    assert extend([1, 2, 3], []) == [1, 2, 3]
    assert extend([1], [4]) == [1, 4]
    print("Great your solution works!")


test_extend()


def test_extend():
    assert extend([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert extend([4, 5, 6], [1, 2, 3], ) == [4, 5, 6, 1, 2, 3]
    assert extend([], [4, 5, 6]) == [4, 5, 6]
    assert extend([1, 2, 3], []) == [1, 2, 3]
    assert extend([1], [4]) == [1, 4]
    print("Great your solution works!")


def is_prime(n):
    """
    Дано число n.
    Если n простое число верните True, иначе False.
    Определние простого числа https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE
    """
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        n = True
    else:
        n = False
    return n


def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(24) is False
    assert is_prime(5) is True
    assert is_prime(0) is False
    assert is_prime(107) is True
    assert is_prime(19) is True
    print("Great your solution works!")

test_is_prime()
