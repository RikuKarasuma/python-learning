import string
from string import Template
import itertools
import collections
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from collections import deque
from enum import Enum, unique
import logging

#class SampleClass:
# Empty class thingy
# pass

class Address:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f"Address(name={self.name}, x={self.x}, y={self.y})"

    def __bytes__(self):
        pass

    def __repr__(self):
        pass

    def __getattr__(self, item):
        if item == "some_param_name":
            return ("A NEW TUPLE", 23)
        else:
            raise AttributeError

    def __eq__(self, other):
        return self.name == other.name


def oop():
    an_andress = Address(name="Donegal Road", x=26, y=32)
    print(an_andress)

def truthy_values(test_param):
    # This is a python comment
    print(f"Hello {test_param}")
    # Falsey:
    # False and None evaluate to false.
    # Numeric zero values: 0, 0.0, 0j.
    # Decimal(0) Fraction(0, x).
    # Empty sequences/collections '', (), [], {}.
    # Empty sets and ranges: set(), range(0).

    # Truthy"""
    # Boolean Operation   |   RESULT.
    # X and Y             |  true if X and Y are both true
    # X or Y              |  true if either X or Y are true
    # not X               |  true if X is false

    # Dictionary i.e map
    x = {"key": 2}
    # List"""
    y = []
    print(f"Is map truthy {bool(x)}")
    print(f"Is list truthy {bool(y)}")

def strings_vs_bytes():
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = " This is a string "
    print(s + b.decode("utf-8"))

    b2 = s.encode("utf-8")
    print(b + b2)

    b3 = s.encode("utf-32")
    print(b2 + b3)


def template_strings():
    template = "You're watching {0} by {1}"
    actual = template.format("Lost", "J. J. Abrams,")
    print(actual)

    templ = Template("You're watching ${title} by ${author}")
    actual_1 = templ.substitute(title="Lost", author="J. J. Abrams, Jeffery Lieber")
    print(actual_1)

    data = {
        "author" : "Jeffery Lieber, Damon Lindelof",
        "title" : "Lost"
    }
    actual_2 = templ.substitute(data)
    print(actual_2)

def any_function():
    list1 = [1, 2, 3, 4, 5, 6]

    # Will print true because every value is > 0, equivalent to OR.
    print(any(list1))

def all_function():
    list1 = [1, 2, 3, 0, 4, 5]

    # Will print false because not every value is > 0, equivalent to
    # AND.
    print(all(list1))


def iteration():
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # Creates iterator, get first three days.
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))

    # Read from file, use iterator for each line.
    with open(
        "address-test.txt",
        "r"
    ) as fp:
        for line in iter(fp.readline, ''):
            print(line)

    # Loop over collection
    for m in days:
        print(m)

    # Loop over w/ index
    for m in range(len(days)):
        print(m, days[m])

    # Loop using enumerate
    for i,m in enumerate(daysFr, start=1):
        print(i, m)

    # Zip numerous collections
    for m in zip(days, daysFr):
        print(m)

def filter_func(x):
    return x % 2 != 0

def filter_upper_func(x):
    return not x.isupper()

def squares(x):
    return x ** 2


def transform_functions():
    nums = [1, 23, 4, 6, 7, 8, 3, 4, 5, 9, 3, 7]

    oddNums = filter(filter_func, nums)

    for m in oddNums:
        print(m)

    chars = "abcDEFWfalekKkdKEde"

    lowercase = filter(filter_upper_func, chars)
    for m in lowercase:
        print(m)

    squared = list(map(squares, nums))

    for m in squared:
        print(m)


def iter_tools():
    seq1 = ["Joe", "John", "Mike"]
    # Iterator
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))

    # Counter
    count1 = itertools.count(8)
    print(next(count1))
    print(next(count1))

    # Accumulator
    vals = [20, 340, 2, 50, 20, 40]
    acc = itertools.accumulate(vals, min)
    print(list(acc))

    # Chain
    x = itertools.chain("ABCD", "!2314")
    print(list(x))

    # Drop while
    x = itertools.dropwhile(filter_func, vals)
    print(list(x))

    # Take while
    x = itertools.takewhile(filter_func, vals)
    print(list(x))


def function_documentation():
    """function_documentation --> Testing the documentation language feature.

    :return:
    """

def function_with_variable_params(*numbers):
    return sum(list(numbers))


def lambda_functions():
    vals = [20, 340, 2, 50, 20, 40]
    print(list(map(lambda t: t * t, vals)))
    print(list(map(lambda t: t ** t, vals)))

def keyword_only_function(arg1, arg2, *, suppressExceptions=False):
    pass

def basic_collections():
    list = [] # List
    tuple = () # Tuple, immutable
    set = {} # Distinct
    map = [] # Dictonary key-value pair

def advanced_collections():
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1.x, p2.y)

    # Replacement
    p1 = p1._replace(x=100)
    print(p1)

    # Default Dic
    # Adds the key when accessed
    fruits = [
        "apple", "pear", "orange", "banana",
        "apple", "grape", "banana", "tangerine"
    ]

    fruit_counter = defaultdict(int)

    for fruit in fruits:
        fruit_counter[fruit] += 1

    for (k, v) in fruit_counter.items():
        print(f"Key {k} = {v}")

    # Counter
    class1 = [
        "Bob", "Becky", "Chad" "Darcy", "Frank", "Hannah", "Kevin", "James",
        "James", "Melanie", "Penie", "Steve"
    ]

    class2 = [
        "Bob", "Becky", "Chad" "Darcy", "Frank", "Hannah", "Kevin", "James",
        "James", "Melanie", "Penie", "Steve", "Bob", "Becky", "Chad" "Darcy",
        "Frank", "Hannah", "Kevin", "James", "James", "Melanie", "Penie", "Steve"
    ]

    c1 = Counter(class1)
    c2 = Counter(class2)

    print(c2["James"], " Named James.")

    print(sum(c1.values()))
    print((c2.most_common()))


    print(c1 & c2)

    # Ordered Dictionary
    sports_teams = [
        ("Royals", (18, 12)), ("Rockets", (24, 6)),
        ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
        ("Kings", (15, 15)), ("Chargers", (20, 10)),
    ]

    sorted_teams = sorted(sports_teams, key=lambda t: [1][0], reverse=True)
    print(sorted_teams)

    teams = OrderedDict(sorted_teams)
    print(teams)

    tm, wl = teams.popitem(False)
    print("Top team: ", tm, wl)

    # Deque
    d = collections.deque(string.ascii_lowercase)

    print("Item count:", str(len(d)))

    for elem in d:
        print(elem, end=",")

    d.pop()
    d.popleft()

    d.append(2)
    d.appendleft(1)

@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4

def advanced_classes():
    # Enums
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))
    print(Fruit.APPLE.name)
    print(Fruit.APPLE.value)

def comparisons():
    address_1 = Address(name="address", x=1, y=2)
    address_2 = Address(name="address", x=4, y=3)
    print(address_1 == address_2)

def logging1():
    fmtstr = "%(asctime)s: %(levelname)s: %(funcName)s Line: %(lineno)d %(message)s"
    logging.basicConfig(level=logging.DEBUG, filename="./output.log", format=fmtstr, filemode="w")

    logging.debug("This is useful debugging info")
    logging.info("General info")
    logging.warning("A warning message")
    logging.error("Error message")
    logging.critical("Serious error message occurred")

    extData = {
        'user': 'joem@example.com'
    }
    logging.critical("ERROR: ", extra=extData)

def comprehensions():
    """Example"""
    # list ( map ( fahrenheitToCelsius, [32, 65, 104, 212]))
    # shortened
    # [(t * 9/5) + 32 for t in [32, 65, 104, 212] ]
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    evenSquared = list(
        map(lambda e: e**2, filter(lambda e: 4 < e < 16, evens))
    )
    print(evenSquared)

    # comprehension ways
    evenSquared1 = [e ** 2 for e in evens]
    print(evenSquared1)

    evenSquared2 = [e ** 2 for e in evens if 4 < e < 16]
    print(evenSquared2)

    tempDicct = {t: (t*9/5) + 32 for t in odds if t <= 11}
    print(tempDicct)

    oddsSet = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 19, 1, 3, 5, 7]
    unique = {(t*9/5) + 32 for t in oddsSet}
    print(unique)






def main():
    truthy_values("TestData1")
    strings_vs_bytes()
    oop()
    template_strings()
    any_function()
    all_function()
    iteration()
    transform_functions()
    iter_tools()
    print(function_documentation.__doc__)
    print(function_with_variable_params(4, 7))
    lambda_functions()
    keyword_only_function(1, 2, suppressExceptions=True)
    advanced_collections()
    advanced_classes()
    comparisons()
    logging1()
    comprehensions()


main()