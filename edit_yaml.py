#from pathlib import Path
#from ruamel.yaml import YAML
#import sys
#import yaml

#myfile = Path('test.yaml')
#myfile.touch(exist_ok=True)#

#with open('test.yaml','w') as file:
   
#   documents = yaml.dump(dict_file, file)#

#yaml = YAML()
#with open('test.yaml') as file:
#    code = yaml.load(file)
#    #code['models']['undbt']['un_quickbooks']['+schema'] = 'kitty'
#    code['name'] = 'kitties'
#    code['sports'][2] = 'cow'
#    #code['sports'].append('biathalon')
#    #print(code['sports'])
#    yaml.dump(code, sys.stdout)

import pathlib
from ruamel.yaml import YAML

yaml = YAML()
#-yaml.preserve_quotes = True
#-with open('test.yaml','+r') as fp:
#-    code = yaml.load(fp)
#-    #print(code)
#-    #code['name'] = 'Bob'
#-    code['sports'][3] = 'kitty'
#-    yaml.dump(code, fp)


mf = pathlib.Path('dbt_project.yml')
doc = yaml.load(mf)

#doc['name'] = 'mike'

def deref_multi(data, keys):
    return deref_multi(data[keys[0]], keys[1:]) \
        if keys else data

def deref_multi(data, keys):
    return deref_multi(data[keys[0]], keys[1:]) \
        if keys else data

last = deref_multi(doc, ['name'])
print(last)
yaml.dump(doc, mf)
