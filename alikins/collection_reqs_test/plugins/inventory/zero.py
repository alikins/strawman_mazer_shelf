
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    inventory: zero
    version_added: "2.8"
    short_description: Zero inventory is zero
    description:
        - Just zero inventory dude.
'''


from ansible.plugins.inventory import BaseInventoryPlugin


# all paths lead to zero
class InventoryModule(BaseInventoryPlugin):
    NAME = 'zero'
