from jinja2 import Environment, FileSystemLoader, FunctionLoader

persons = [
    {'name': 'Алексей', 'old': 18, 'weight': 78.5},
    {'name': 'Николай', 'old': 28, 'weight': 82.3},
    {'name': 'Иван', 'old': 33, 'weight': 94.0}
]

file_loader = FileSystemLoader('traindir')
env = Environment(loader=file_loader)

tm = env.get_template("page.htm")
msg = tm.render(title = "Любитель пива", domain = 'Civilization5.org/about_me')

print(msg)