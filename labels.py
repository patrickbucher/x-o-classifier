#!/usr/bin/env python3

import os

with open('labels.csv', 'w') as csv:
    directory = 'png'
    csv.write('path,label\n')
    for f in sorted(os.listdir(directory)):
        path = os.path.join(directory, f)
        label = f[0]
        csv.write(f'{path},{label}\n')
