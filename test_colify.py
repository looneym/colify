import pytest

from colify import Colify

spain = ["madrid", "barcelona", "bilbao", "Malaga"]
italy = ["rome", "florence", "milan", "venice", "palermo", "padua"]
france = ["paris", "lyon", "toulouse", "nantes"]
countries = {}
countries['spain'] = spain
countries['italy'] = italy
countries['france'] = france

c = Colify(countries)
c.print_headers() 
c.print_body()
