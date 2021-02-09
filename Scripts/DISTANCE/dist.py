import numpy as np
from scipy.spatial.distance import pdist, mahalanobis
from statistics import NormalDist
from dtw import dtw
from scipy.stats import multivariate_normal
import pandas as pd
#欧氏距离
def euclidean_distance(x, y):
    xx = np.vstack([x, y])
    d2 = pdist(xx)
    return d2

#曼哈顿距离
def manhattan_distance(x, y):
    xx = np.vstack([x, y])
    d2 = pdist(xx, 'cityblock')
    return d2

#切比雪夫距离
def chebyshev_distance(x, y):
    xx = np.vstack([x, y])
    d2 = pdist(xx, 'chebyshev')
    return d2

#闵氏距离
def minkowski_distance(x, y, p):
    xx = np.vstack([x, y])
    d2 = pdist(xx, 'minkowski', p=p)
    return d2

#马氏距离
def mahalanobis_distance(p, distr):
    cov = np.cov(distr,rowvar=False)
    avg_distri = np.average(distr,axis=0)
    dis = mahalanobis(p,avg_distri,cov)
    return dis

#1维高斯
def overlap_1d(mu1,mu2,sigma1,sigma2,step=1):

    ovp = NormalDist(mu=mu1, sigma=sigma1).overlap(NormalDist(mu=mu2, sigma=sigma2))

    return ovp

#2维高斯
def overlap_2d(mu1,mu2,sigma1,sigma2,step=1):

    gauss1 = multivariate_normal(mean=mu1, cov=sigma1)
    gauss2 = multivariate_normal(mean=mu2, cov=sigma2)

    x = []
    a = max(sigma1[0][0],sigma1[1][1])
    # print(a)
    range_x = 5*a
    range_y = 5*a
    for i in np.arange(mu1[0]-1*range_x,mu1[0]+range_x,step):
        for j in np.arange(mu1[1]-1*range_y, mu1[1]+range_y, step):
            x.append([i,j])

    pdf1 = sum(gauss1.pdf(x)*gauss2.pdf(x)*step**2)
    pdf2 = np.math.sqrt(sum(gauss1.pdf(x) ** 2*step**2))*np.math.sqrt(sum(gauss2.pdf(x) ** 2*step**2))
    ovp = (pdf1/pdf2)

    return ovp


def cosine_similarity(x, y, norm=False):
    """ 计算两个向量x和y的余弦相似度 """
    assert len(x) == len(y), "len(x) != len(y)"
    zero_list = [0] * len(x)
    if x == zero_list or y == zero_list:
        return float(1) if x == y else float(0)

    # method 1
    res = np.array([[x[i] * y[i], x[i] * x[i], y[i] * y[i]] for i in range(len(x))])
    cos = sum(res[:, 0]) / (np.sqrt(sum(res[:, 1])) * np.sqrt(sum(res[:, 2])))

    return 0.5 * cos + 0.5 if norm else cos  # 归一化到[0, 1]区间内



if __name__ == '__main__':
    # x = np.array([[1,2],[2,3],[4,5],[3,2],[2,1],[1,2]])
    # print(x)
    # d = np.array([2,3])
    # print(mahalanobis_distance(d,x))
    # mu1 = [0, 0]
    # mu2 = [0, 0]
    # sigma1 = [[1, 0], [0, 1]]
    # sigma2 = [[1, 0], [0, 1]]
    # o = overlap_2d(mu1,mu2,sigma1,sigma2)
    # print(o)
    # d = cosine_similarity([1, 2, 2, 1, 1, 1, 0], [1, 2, 2, 1, 1, 2, 1])
    # print(d)

    aa = np.array([2, 3, 9, 6, 8])
    bb = np.array([5, 6, 3, 7, 9])
    cc = np.array([aa, bb])

    cc_mean = np.mean(cc, axis=0)  # axis=0,表示按列求均值 ——— 即第一维
    cc_std = np.std(cc, axis=0)
    cc_zscore = (cc - cc_mean) / cc_std  # 标准化

    cc_zscore_corr = np.corrcoef(cc_zscore)  # 相关系数矩阵
    print(cc_zscore_corr)
