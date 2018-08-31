#!/usr/bin/python3
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


def pie(label, data):
    # 書式
    plt.style.use('ggplot')
    plt.rcParams.update({'font.size': 15})

    # 各種パラメータ
    size = (9, 5)
    col = cm.Spectral(np.arange(len(data)) / float(len(data)))

    # pie
    plt.figure(figsize=size, dpi=100)
    plt.pie(data, colors=col, counterclock=False, startangle=90, autopct=lambda p: '{:.1f}%'.format(p) if p >= 5 else '')
    plt.subplots_adjust(left=0, right=0.7)
    plt.legend(label, fancybox=True, loc='center left', bbox_to_anchor=(0.9, 0.5))
    plt.axis('equal')
    plt.savefig('tt_wr.png', bbox_inches='tight', pad_inches=0.05)
    plt.show()
