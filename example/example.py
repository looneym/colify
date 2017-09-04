from colify.colify import Colify

countries = {}
countries['spain'] = ["madrid", "barcelona", "bilbao", "Malaga"]
countries['italy'] = ["rome", "florence", "milan", "venice", "palermo", "padua"]
countries['france'] = ["paris", "lyon", "toulouse", "nantes"]

c = Colify(countries)
c.colify()
