#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

for i in range(27):
    plt.subplot(9, 3, i+1)
    plt.imshow(np.random.rand(50, 50))
    # plt.title(i + 1)
    plt.axis('off')
    # plt.yticks([])
    plt.subplots_adjust(hspace=.001)
    plt.subplots_adjust(wspace=.001)
