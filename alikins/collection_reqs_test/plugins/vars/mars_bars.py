from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    vars: mars_bars
    version_added: "2.8"
    short_description: Jars Of Mars Bars Vars
    description:
        - vars of mars and bars
'''

from ansible.plugins.vars import BaseVarsPlugin

FOUND = {}


class VarsModule(BaseVarsPlugin):

    def get_vars(self, loader, path, entities, cache=True):
        super(VarsModule, self).get_vars(loader, path, entities)

        data = {'mars_uk': {'origin': 'United Kingdom',
                            'nougat': 'good'},
                'mars_us': {'origin': 'United States',
                            'nougat': 'bad'},
                'mars_aliases': ['milky_way']}
        return data
