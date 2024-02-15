from string import Template
import itertools


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


main()