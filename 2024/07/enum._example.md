https://docs.python.org/3/library/enum.html
https://docs.python.org/3/howto/enum.html
https://www.kdnuggets.com/python-enum-how-to-build-enumerations-in-python
https://www.luu.io/posts/dont-use-booleans
https://en.wikipedia.org/wiki/Enumerated_type


### Basics
- list as enum
- dict as enum
- `from enum import Enum`
- create by statement
  - list
  - dict
- create by class
- int value
- string value
- get value
- get name
- ref by value
- ref by key
- iterate

### Intermediate
- auto value
- Alias
- `@unique`


### Advanced
- override `_generate_next_value_(name, start, count, last_values)`
- `init()`
- `_missing_()`
- `__repr__`
- `__str__`
- `namedtuple` as value
- dataclass mixin
- `Flag`
- `__members__`
