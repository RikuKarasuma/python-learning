from string import Template


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
def main():
    truthy_values("TestData1")
    strings_vs_bytes()
    oop()
    template_strings()

main()