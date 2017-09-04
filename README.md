# Colify

Print a dictionary of arrays as vertical columns in the terminal

### Install

`pip install colify`

### Usage

```python
from colify.colify import Colify

countries = {}
countries['spain'] = ["madrid", "barcelona", "bilbao", "Malaga"]
countries['italy'] = ["rome", "florence", "milan", "venice", "palermo", "padua"]
countries['france'] = ["paris", "lyon", "toulouse", "nantes"]

c = Colify(countries)
c.colify()
# Output:
# |    madrid |      rome |     paris |
# | barcelona |  florence |      lyon |
# |    bilbao |     milan |  toulouse |
# |    Malaga |    venice |    nantes |
# |           |   palermo |           |
```
