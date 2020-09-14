'''题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。'''

with open('97_write_file.txt', 'w') as f:
    while True:
        context = input()
        f.write((context).rstrip('#') + '\n')
        if '#' in context:
            break
