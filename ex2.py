from jinja2 import Template

cars = [{'model': 'Ауди', 'price': 23_000},
          {'model': "Шкода", 'price': 17_300},
          {'model': "Вольво", 'price': 44_300},
          {'model': "Фольксваген", 'price': 21_300}
          ]


digs = [1, 2, 3, 4, 5]
tpl = "Суммарная цена автомобилей {{ cs | max }}"
tm = Template(tpl)
msg = tm.render(cs = digs)

print(msg)