import jinja2

data = """Модуль Jinja2 вместо
определения {{ name }}
подставляет соответствующее значение"""

tm = jinja2.Template(data)
msg = tm.render(name='Илья')

print(msg)