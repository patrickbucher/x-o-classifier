#!/usr/bin/env python3

import math
import os

import imageio
import numpy as np
import pandas as pd


def sigmoid(x):
    return 1 / (1 + math.e ** -x)

labels = pd.read_csv('predict.csv')

images = labels['path'].apply(lambda p: imageio.imread(p).flatten()).to_numpy()
inputs = np.zeros((len(images), len(images[0])))
for i, image in enumerate(images):
    inputs[i,:] = image

labels = labels['label']
values = ['x', 'o']
labels_one_hot = {l: (labels == l).astype(int) for l in values}

weights_file = 'weights.csv'
theta = np.loadtxt(weights_file, delimiter=',')
print(f'loaded weights {theta} as CSV to {weights_file}')

x = (inputs - inputs.mean()) / inputs.std()
predictions = sigmoid(x.dot(theta)).round()
correct = len(labels_one_hot['x'] == predictions)
accuracy = correct / len(labels_one_hot['x'])
print(f'accuracy={accuracy:.3f}')
