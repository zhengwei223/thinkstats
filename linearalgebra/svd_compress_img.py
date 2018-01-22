import time

import numpy as np
from PIL import Image


def rebuild(u, sigma, v, per=0.9):
    'per：奇异值占比'
    m = len(u)
    n = len(v)
    a = np.zeros((m, n))
    sigma_sum = int(sum(sigma))
    cur_sum = 0
    k = 0
    while cur_sum <= sigma_sum * per:
        # 取1列
        uk = u[:, k].reshape(m, 1)
        # 取一行
        vk = v[k].reshape(1, n)

        a += sigma[k] * np.dot(uk, vk)

        cur_sum += sigma[k]  # 累加奇异值
        k += 1
    a[a < 0] = 0
    a[a > 255] = 255
    print("k/n==%d/%d==%.2f" % (k, n, k / n))
    return np.rint(a).astype("uint8")


def rebuild2(u, sigma, v, k):
    "r:前k维"
    uk = u[:, :k]
    sigma_k = np.diag(sigma[:k])
    vk = v[:k, :]

    dot1 = np.dot(uk, sigma_k)
    return np.dot(dot1, vk)


now = time.clock()
pic = Image.open('/Users/zhengwei/Pictures/zxt.jpg', 'r')
# 灰度转换
pic = pic.convert("L")
pic.show()
# 转换为矩阵
pic_arr = np.array(pic)
print(pic_arr.shape)

# svd
# u, sigma, v = np.linalg.svd(pic_arr[:, :, 0])
# R = rebuild(u, sigma, v)
# u, sigma, v = np.linalg.svd(pic_arr[:, :, 1])
# G = rebuild(u, sigma, v)
# u, sigma, v = np.linalg.svd(pic_arr[:, :, 2])
# B = rebuild(u, sigma, v)
# I = np.stack((R, G, B), 2)

# SVD
u, sigma, v = np.linalg.svd(pic_arr[:, :])
print(sigma.shape)
# 重构图像，返回灰度矩阵，per参数为前k维的权重（奇异值）之和
L = rebuild(u, sigma, v)
Image.fromarray(L).show()

# L = rebuild2(u, sigma, v, k=64)
# Image.fromarray(L).show()

# L = rebuild2(u, sigma, v, k=128)
# Image.fromarray(L).show()

print('运算时间：%s' % (time.clock() - now))  # 整体运行时间)
