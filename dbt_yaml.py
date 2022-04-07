import json
import pathlib
from ruamel.yaml import YAML
from functools import partial
import collections.abc

class DbtYaml:
    def __init__(self, file):
        self._file = file
        self.yml_file = False
        self.yml_data = False

    def __enter__(self):
        self.yml_file = pathlib.Path(self._file)
        yaml = YAML()
        self.yml_data = yaml.load(self.yml_file)
        return self

    def getYamlObj(self):
        return self.yml_data['config-version']

    def changeValue(self, value, ref):
        self.yml_data.update({'name','matt'})
        #print(type(self.yml_data['models']))
        #self.yml_data['models']['undbt']['un_quickbooks']['+schema'] = 'kitty'
        #for item in ref:
            #print(item)
            #place_holder = self.get(yml_data, item]
            #print(place_holder is self.yml_data)
        #self.yml_data[place_holder] = value
        
    def getValue(self, *nodes):
        '''
            method to get the value of an element from a node tree
            params: list of nodes to transverse to get an element
        '''
        
        for node in nodes:                                                                                                  
            level = self.get_data(self.yml_data,node)

        return level

    def get_data(self, level, node):                                                                                          
        return level[node]

    def __exit__( self, exc_type, exc_val, exc_tb ):
        yaml = YAML()
        yaml.dump(self.yml_data, self.yml_file)
        

with DbtYaml('dbt_project.yml') as dbt_yaml:
    #node = type(dbt_yaml.getValue('name'))

    #dbt_yaml.changeValue('dude',node)
    #print(node)
    dbt_yaml.changeValue('evan',['name'])
    #value['+schema'] = 'kitty cats'
    #print(json.dumps(dbt_yaml.getYamlObj(),indent=4))

