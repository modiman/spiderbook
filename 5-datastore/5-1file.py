import csv

import requests
from pyquery import PyQuery as pq
import json
class DataStore:
    def __init__(self):
        self.url = 'https://www.zhihu.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
            }
        #self.html = requests.get(self.url, headers=self.headers).text
    def store_txt(self):
        #doc = pq(self.html)
        items = [1,2,3]
        for item in items:
            question = '[1,2,3]'
            author = '[11,2,3]'
            answer = '[1111,2,3]'
            file = open('explore.txt', 'a', encoding='utf-8')
            file.write('\n'.join([question, author, answer]))
            file.write('\n' + '=' * 50 + '\n')
            file.close()
        # 简化写法
        with open('explore.txt', 'a', encoding='utf-8') as file:
            file.write('\n'.join([question, author, answer]))
            file.write('\n' + '=' * 50 + '\n')
    ## json中的键值通常使用双括号，单括号会报错
    def store_json(self):
        # 读取json
        str = '''
        [{
            "name": "王瑞",
            "gender": "male",
            "birthday": "1992-10-18"
        }, {
            "name": "Selina",
            "gender": "female",
            "birthday": "1995-10-18"
        }]
        '''
        data = json.loads(str)
        print(data)
        print(type(data))
        ## 取值有两种方式，推荐get,当值不存在时返回None而非报错
        print(data[0].get('age'))
        print(data[0]['name'])

        ## 输出json
        # 我们还可以调用 dumps 方法将 JSON 对象转化为字符串。
        # 例如，将上例中的列表重新写入文本：
        # w会擦除原有数据

        with open('data.json', 'w') as file:
            file.write(json.dumps(data))

        '''
        如果想保存 JSON 的格式，可以再加一个参数 indent，代表缩进字符个数。示例如下：
        with open('data.json', 'w') as file:
             file.write(json.dumps(data, indent=2))
        
        '''
        # a不擦除原有数据
        with open('data.json', 'w') as file:
            file.write(json.dumps(data, indent=2))
        # 为了保存中文字符，添加一个参数
        with open('data.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))
    def store_csv(self):
        # 逐行写入
        with open('data.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['id', 'name', 'age'])
            writer.writerow(['10001', 'Mike', 20])
            writer.writerow(['10002', 'Bob', 22])
            writer.writerow(['10003', 'Jordan', 21])
        # 如果想修改列与列之间的分隔符，可以传入 delimiter 参数，其代码如下
        with open('data.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')#  改为空格
            writer.writerow(['id', 'name', 'age'])
            writer.writerow(['10001', 'Mike', 20])
            writer.writerow(['10002', 'Bob', 22])
            writer.writerow(['10003', 'Jordan', 21])
        # 写入多行
        with open('data.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            # 写入表头
            writer.writerow(['id', 'name', 'age'])
            # 写入数据
            writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])
        # 写入字典
        with open('data.csv', 'w') as csvfile:
            fieldnames = ['id', 'name', 'age']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
            writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
            writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})
        # 写入中文
        with open('data.csv', 'w',encoding='utf-8') as csvfile:
            fieldnames = ['id', 'name', 'age']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'id': '10001', 'name': '王瑞', 'age': 20})
            writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
            writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})
    def read_csv(self):
        with open('data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)


if __name__ == '__main__':
    ds = DataStore()
    ds.read_csv()