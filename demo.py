#!/usr/bin/env python3

import math
import os
import sys

import imageio
import numpy as np


def sigmoid(x):
    return 1 / (1 + math.e ** -x)

# usage: ./demo.py [16x16 png file]

imagefile = sys.argv[1]
image = imageio.imread(imagefile).flatten()

weights_file = 'weights.csv'
theta = np.loadtxt(weights_file, delimiter=',')

x = (image - image.mean()) / image.std()
is_x = sigmoid(x.dot(theta))
is_o = 1 - is_x
print(f'{imagefile}:')
print(f'\tP("x")={is_x * 100:.2f}%')
print(f'\tP("o")={is_o * 100:.2f}%')
