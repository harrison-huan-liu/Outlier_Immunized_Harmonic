import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
from collections import Counter


def bar_plot(data):
    data_1, data_2, data_3 = data['CN'].values, data['EMCI'].values, data['LMCI'].values
    # remove nan
    data_1 = [data_1_ for data_1_ in data_1 if data_1_ == data_1_]
    data_2 = [data_2_ for data_2_ in data_2 if data_2_ == data_2_]
    data_3 = [data_3_ for data_3_ in data_3 if data_3_ == data_3_]
    # print(data_amy_1)

    data_1 = remove(data_1)
    data_2 = remove(data_2)
    data_3 = remove(data_3)

    B_1 = np.trunc(data_1)
    B_2 = np.trunc(data_2)
    B_3 = np.trunc(data_3)
    # print(B_3)

    C_1 = B_1.astype(int)
    C_2 = B_2.astype(int)
    C_3 = B_3.astype(int)

    D_1 = C_1.tolist()
    D_2 = C_2.tolist()
    D_3 = C_3.tolist()
    print(D_1)

    result_1 = {}
    for i in set(D_1):
        result_1[i] = D_1.count(i)
    print(result_1)
    result_2 = {}
    for i in set(D_2):
        result_2[i] = D_2.count(i)
    print(result_2)
    result_3 = {}
    for i in set(D_3):
        result_3[i] = D_3.count(i)
    print(result_3)
    print(type(result_3))

    bins = np.linspace(200, 900, 24)
    # x = np.linspace(1, 31, 31)

    n2, bins2, patches2 = plt.hist(D_1, bins, alpha = 0.5, density = True, histtype='bar', color='#FF0000')
    # print(n2)
    # print(bins2)
    # print(patches2)

    # plot the line
    # plt.plot(x,n,color='red',label='CN')

    # plot the curve
    mu2 = 451.3279751 # 8.4221
    sigma2 = 96.27814189 # 3.5319
    bins2 = np.linspace(200, 900, 320)
    y2 = norm.pdf(bins2, mu2, sigma2)
    l2 = plt.plot(bins2, y2, color='#FF0000', label='CN')

    # parameter = np.polyfit(x, n, 2)
    # y2 = parameter[0] * x ** 2 + parameter[1] * x + parameter[2] #parameter[0] * x ** 3 +
    # plt.plot(x, y2, color='red', label='CN')

    n1, bins1, patches1 = plt.hist(D_2, bins, alpha=0.5, density=True, histtype='bar', color='#FF7400')
    mu1 = 489.902845  # 8.1479
    sigma1 = 114.8732702  # 3.4626
    bins1 = np.linspace(200, 900, 320)
    y1 = norm.pdf(bins1, mu1, sigma1)
    l1 = plt.plot(bins1, y1, color='#FF7400', label='EMCI')

    n3, bins3, patches3 = plt.hist(D_3, bins, alpha = 0.5, density = True, histtype='bar', color='#009999')
    mu3 = 568.0126874 # 9.8307
    sigma3 = 184.3013494 # 4.2601
    bins3 = np.linspace(200, 900, 320)
    y3 = norm.pdf(bins3, mu3, sigma3)
    l3 = plt.plot(bins3, y3, color='#009999', label='LMCI')

    plt.legend([patches2, patches1, patches3], ["CN", "EMCI", "LMCI"], loc='upper right')


def remove(box_1):
    Q1 = np.percentile(box_1, 25)
    Q3 = np.percentile(box_1, 75)

    low_whisker = Q1 - 1.5 * (Q3 - Q1)
    up_whisker = Q3 + 1.5 * (Q3 - Q1)

    outlier_num = []
    # find outlier
    for i in range(len(box_1)):
        if (float(box_1[i]) >= up_whisker) or (float(box_1[i]) <= low_whisker):
            outlier_num.append(i)

    for i in range(len(outlier_num)):
        # print(outlier_num[i]-i)
        del box_1[outlier_num[i]-i]

    return box_1


datafile1 = 'energy_amy.xlsx'
data1 = pd.read_excel(datafile1)
plt.figure(figsize=(6, 5))
bar_plot(data1)
plt.savefig('bar_amy.eps', dpi=300, format='eps')
plt.show()
