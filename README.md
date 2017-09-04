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
```

Output:

![image](https://user-images.githubusercontent.com/12705417/30010822-8f8aee8e-912a-11e7-97b5-351379385c52.png)
