# docstring для функций, модулей и классов
from typing import Dict, Optional, Union
from typing import Dict
from typing import Tuple
from typing import Set, FrozenSet
from typing import List
from typing import Any
from typing import Optional


def get_even(lst):
    '''Функция 
создаёт список 
из чётных чисел'''
    even_lst = []
    for elem in lst:
        if elem % 2 == 0:
            even_lst.append(elem)
    return even_lst

# Аннотации для функции: a,b - должны быть int, return возвращает int


def add_numbers(a: int, b: int) -> int:
    return a + b


# Optional

num: Optional[int] = None  # или стр или none можно просто Optional[int]
word: Optional[str] = None
num: int | None = None
word: str | None = None
# Any не знаю зачем если у питона и так динамическая типизация
value: Any
value = 10
print(value)
value = [1, 2, 3]
print(value)
value = {'hi': 'привет'}
print(value)

# union
param: int | float | str

# list

words: list[str] = ["hello", "world"]

# set frozenset

words: Set[str] = {"hello", "world"}
numbers: FrozenSet[int] = frozenset([1, 2, 2, 1])

# tuple аннотируем каждый элемент

words: Tuple[str, int] = ("hello", 300)

# Dict
person: dict[str, str] = {"first_name": "John", "last_name": "Doe"}

# Совокупность нескольких аннотаций


def foo(bar: Dict[Union[str, int], Optional[str]]) -> bool:
    return True


def foo(bar: dict[str | int, str | None]) -> bool:
    return True
