from jinja2 import Environment, FileSystemLoader
from os import listdir, path
from json import loads
import sys

file_loader = FileSystemLoader(path.join(path.dirname(__file__),'templates'))
env = Environment(loader=file_loader)

try:
    template = env.get_template('template.md')
except Exception as e:
    template = env.get_template('sample_template.md')

workflows = []
print(__file__)
print(path.dirname(__file__))
print(path.dirname(path.dirname(__file__)))
dirs = listdir(sys.argv[1])
i=0
for dir in dirs:
        if path.isdir(dir) and dir not in ['.github','.git','templates']:
            files = listdir(dir)
            for wf in files:
                with open(path.join(dir,wf)) as f:
                    d = loads(f.read())
                if '!#NODOC' not in d['workflow']['properties']['description']:
                    i+=1
                    workflows.append({
                        'index': i,
                        'name': d['workflow']['name'],
                        'description': d['workflow']['properties']['description'],
                        'dir': dir
                    })

output = template.render(workflows=workflows)

with open(path.join(path.dirname(path.dirname(__file__)),'README.md'),'w', encoding="utf-8") as f:
    f.write(output)
