from jinja2 import Template

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

n = 'Федор'
a = 28

per = Person(n, a)

tm = Template('Мне {{ p.age * 2 }} лет и зовут {{ p.name }}')
msg = tm.render(p = per)

print(msg)