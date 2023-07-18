from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('traindir')
env = Environment(loader = file_loader)

template = env.get_template('about.htm')

output = template.render()

print(output)