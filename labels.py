#!/usr/bin/env python3

import os
import sys

# usage: ./labels.py [directory] [csv_file]

directory = sys.argv[1]
csv_file = sys.argv[2]
with open(csv_file, 'w') as csv:
    csv.write('path,label\n')
    for f in sorted(os.listdir(directory)):
        path = os.path.join(directory, f)
        label = f[0]
        csv.write(f'{path},{label}\n')
