#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json
import sys

from ansible.module_utils.newutil import get_stuff


def main():

    res = {
        'success': True,
        'changed': True,
        'lolcats': 50000,
        'stuff': get_stuff()
    }
    print(json.dumps(res))
    sys.exit(0)


if __name__ == "__main__":
    main()
