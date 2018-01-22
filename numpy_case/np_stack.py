import numpy as np
a=[[1,2,3],
   [4,5,6]]
print("列表a如下：")
print(a)

print("增加一维，新维度的下标为0")
c=np.stack(a,axis=0)
print(c)

print("增加一维，新维度的下标为1")
c=np.stack(a,axis=1)
print(c)