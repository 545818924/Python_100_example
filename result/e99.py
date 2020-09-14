'''题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。'''

with open('97_write_file.txt', 'r') as fa:
    a = fa.read()

with open('98_write_file.txt', 'r') as fb:
    b = fb.read()

c = ''.join(sorted(a + b))

with open('99_write_file.txt', 'w') as fc:
    fc.write(c)
