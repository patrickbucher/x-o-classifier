#!/usr/bin/env python3

import math
import os

import imageio
import numpy as np
import pandas as pd


def sigmoid(x):
    return 1 / (1 + math.e ** -x)


def cost(x, y, theta):
    z = x.dot(theta)
    c = -y * np.log(sigmoid(z)) - (1 - y) * np.log((1 - sigmoid(z)))
    j = 1 / len(x) * c.sum()
    return j


labels = pd.read_csv('labels.csv')

images = labels['path'].apply(lambda p: imageio.imread(p).flatten()).to_numpy()
inputs = np.zeros((len(images), len(images[0])))
for i, image in enumerate(images):
    inputs[i,:] = image

labels = labels['label']
values = ['x', 'o']
labels_one_hot = {l: (labels == l).astype(int) for l in values}

alpha = 0.01
iters = 1_000
theta = np.zeros(len(inputs[0]))

# to begin, let's only train an 'x' classifier 

y = labels_one_hot['x']
x = (inputs - inputs.mean()) / inputs.std()
for i in range(iters):
    m = len(inputs)
    p = sigmoid(x.dot(theta))
    theta -= (alpha / m) * x.transpose().dot(p - y)
    c = cost(x, y, theta)
    if i % (iters / 10) == 0:
        print(f'cost={c:.4f}')

predictions = sigmoid(x.dot(theta)).round()
correct = len(labels_one_hot['x'] == predictions)
accuracy = correct / len(labels_one_hot['x'])
print(f'accuracy={accuracy:.3f}')

weights_file = 'weights.csv'
np.savetxt('weights.csv', theta, delimiter=',')
print(f'saved weights {theta} as CSV to {weights_file}')
