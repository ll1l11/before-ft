# -*- coding: utf-8 -*-
import json

d = {
    'b': 2,
    'a': {'c1': 13, 'b1': 12, 'a1': 11},
    'c': 3
}

x = json.dumps(d, sort_keys=True)

print(x)
