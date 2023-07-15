from jinja2 import Template


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


n = 'Федор'
a = 28

per = Person(n, a)

tm = Template('Мне {{ p.getAge() }} лет и зовут {{ p.getName() }}')
msg = tm.render(p=per)

print(msg)
