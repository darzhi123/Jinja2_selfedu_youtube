import jinja2

data = """{%raw%}Модуль Jinja2 вместо
определения {{ name }}
подставляет соответствующее значение{%endraw%}"""

tm = jinja2.Template(data)
msg = tm.render(name='Илья')

print(msg)