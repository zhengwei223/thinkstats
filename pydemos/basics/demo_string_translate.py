'str translate的用法'

# 新建一个转换模式:前两个参数是映射，即第一个参数的每个字符将会被替换成第二个参数对应位置的字符
# 第三个参数是在转换中要去掉的字符
trans1 = str.maketrans('abc','123','t')

print("this people is a girl".translate(trans1))