import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a)
# 所有的行的第三列，本身组成一个行，reshape成三行一列
ak = a[:, 2].reshape(3, 1)
print(ak)
