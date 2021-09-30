def unique(numbers):
    """
    Дна список чисел. Некоторые числа в нем могут повторяться.
    Верните новый список чисел, который состоит из чисел numbers, но уже без повторений.
    """
    unique_numbers = list(set(numbers))
    return unique_numbers


def test_unique():
    assert unique([1, 1, 2, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5]
    assert unique([1, 1, 1, 1]) == [1]
    assert unique([]) == []
    print("Great your solution works!")

test_unique()

def count_words(string):
    """
    Дан список строк strings.
    Нужно для каждой строки посчитать сколько раз она встретилось в списке.
    """
    counts = dict()

    for word in string:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def test_count_words():
    assert count_words(["text", "text", "apple", "orange", "yellow", "orange"]) == {
        "text": 2,
        "orange": 2,
        "yellow": 1,
        "apple": 1
    }
    assert count_words(["text", "text", "text", "text", "text", "orange"]) == {
        "text": 5,
        "orange": 1,
    }
    assert count_words([]) == {}
    print("Great your solution works!")

test_count_words()

def sort_desc(strings):
    """
    Дан список строк. Отсортируйте его в порядке обратном алфавитному.
    """

    a = sorted(strings, reverse=True)
    return a

def test_sort_desc():
    assert sort_desc(["ad", "bd", "aaab", "baa", "badab"]) == ['bd', 'badab', 'baa', 'ad', 'aaab']
    assert sort_desc(["a", "b", "c", "ab", "ac", "bc", "abc"]) == ['c', 'bc', 'b', 'ac', 'abc', 'ab', 'a']
    print("Great your solution works!")

test_sort_desc()

def filter_even(numbers):
    """
    При помощи встроенный функции фильтр, отфильтруйте только четные числа из списка numbers
    в отсортированном по возрастанию порядке
    """
    filter_even = lambda x: x % 2 ==0
    even = sorted(list(filter(filter_even, numbers)))
    return even


def test_filter_even():
    assert filter_even([1, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12]) == [2, 4, 6, 8, 10, 12]
    assert filter_even([2, 2, 4, 6, 6, 8, 10, 12]) == [2, 2, 4, 6, 6, 8, 10, 12]
    assert filter_even([1, 1, 2, 3]) == [2]
    assert filter_even([1, 3, 5]) == []
    print("Great your solution works!")


test_filter_even()