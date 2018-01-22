# f = open('func.py', 'r', encoding='utf-8')
# line = f.readline()
# while len(line) != 0:
#     print(line)
#     line = f.readline()
#
# f.close()

f = open('demo_func.py', 'r', encoding='utf-8')
for i, line in enumerate(f):
    print(line)
f.close()
