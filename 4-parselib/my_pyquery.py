# coding:utf-8
from pyquery import PyQuery as pq

class model:
    def __init__(self):
        self.html = '''
                    <div id="container">
                        <ul class="list">
                             <li class="item-0">first item</li>
                             <li class="item-1"><a href="link2.html">second item</a></li>
                             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
                             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
                             <li class="item-0"><a href="link5.html">fifth item</a></li>
                         </ul>
                     </div>
                    '''
        self.url = 'https://www.baidu.com'
    def hello(self):
        # 传递字符串
        doc = pq(self.html)
        print(doc('li'))
        ## 传递url
        doc = pq(url=self.url)
        print(doc('title').text())
        # 传递本地文件
        doc = pq(filename='test.html')
        print(doc('li'))
    def selector(self):
        doc = pq(self.html)
        print(doc('#container .list li'))
        print(type(doc('#container .list li')))

if __name__ == '__main__':
    doc = pq('https://www.google.com')
    print(doc)