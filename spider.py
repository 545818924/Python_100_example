import os
import requests
from multiprocessing import Pool
from pyquery import PyQuery as pq

url = 'http://www.runoob.com/python/python-exercise-example{num}.html' # 目标站点

# 获取页面
def get_page(url):
    try:
        r = requests.get(url)
        r.encoding = 'utf-8'
        if r.status_code == 200:
            return r.text
        return None
    except:
        print('爬取失败')

# 解析页面
def parse_page(html):
    doc = pq(html)
    content = doc('#content > p:nth-child(3)').text()
    return "'''" + content + "'''" # 将内容全部转换成字符串

# 保存到文件
def save_to_file(num, content):
    folder = 'result___'
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = folder + os.path.sep + "e" + num + '.py' # 文件名 e 开头可被引用
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
            print(path, '保存成功')

# 主函数
def main(num):
    html = get_page(url.format(num=num))
    save_to_file(str(num), parse_page(html))


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [page for page in range(1, 101)]) # 多进程实现
