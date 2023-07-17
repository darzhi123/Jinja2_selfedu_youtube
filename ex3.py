from jinja2 import Template
from pprint import pprint

persons = [
    {'name': 'Алексей', 'old': 18, 'weight': 78.5},
    {'name': 'Николай', 'old': 28, 'weight': 82.3},
    {'name': 'Иван', 'old': 33, 'weight': 94.0}
]

tpl = '''
{%- for user in users -%}
{%- filter upper() %}{{user.name}}{% endfilter %}
{% endfor -%}
'''

tm = Template(tpl)
msg = tm.render(users=persons)

print(msg)
