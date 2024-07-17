from enum import Enum, auto, unique, Flag
from dataclasses import dataclass

# # Dictionary based pseudo enum:
# Colors = {'RED': 1, 'BLUE':2, 'GREEN':1}
# print(Colors['RED'])
# color = 'GREEN'


Colors0 = Enum('Colors', ['RED', 'BLUE', 'GREEN'])
Colors1 = Enum('Colors', {'RED': 'stop', 'BLUE': 'caution', 'GREEN': 'go'})


@dataclass
class ColorAttrib:
    abbr: str
    desc: str


# @unique
class Colors2(ColorAttrib, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return chr(ord('A') + count)

    RED = auto(), 'Red'
    BLUE = auto(), 'Blue'
    GREEN = auto(), 'Green'
    RD = RED
    BL = BLUE
    GN = GREEN

    def __init__(self, abbr, desc):
        self.abbr = abbr
        self.desc = desc

    @classmethod
    def _missing_(cls, value:str):
        for member in cls:
            # if member.name == value.upper() or member.abbr == value:
            if member.desc.lower() == value.lower() or member.abbr == value:
                return member
        return None

    def __str__(self):
        return self.name.lower()


class Colors3(Flag):
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    YELLOW = RED | GREEN
    CYAN = GREEN | BLUE
    VIOLET = RED | BLUE
    WHITE = RED | GREEN | BLUE
    BLACK = RED & GREEN & BLUE


def main():
    for color in Colors0:
        print('color0:', color, color.value, color.name)

    for color in Colors1:
        print('color1:', color, color.value, color.name)

    print(Colors1.BLUE.value)
    print(Colors2.BLUE.value)

    mycolor: Colors2 = Colors2.RED

    print("repr:", repr(Colors2.RED))
    print("value:", Colors2.RED.value)
    print("name:", Colors2.RED.name)
    print("str:", Colors2.RED)

    print("ref by index value:", Colors2('B'))
    print("ref by key:", Colors2['BLUE'])
    print("ref by key:", Colors2['BL'])
    print("ref by index value lc:", Colors2('blue'))

    for color in Colors2:
        print('color2:', color, color.value, color.name)

    for name, color in Colors3.__members__.items():
        print('color3:', color, color.value, name)


if __name__ == '__main__':
    main()
