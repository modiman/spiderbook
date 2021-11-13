from lxml import etree

class model:
    def __init__(self):
        self.filename = 'test.html'
        self.text = '''
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
        '''

        pass
    def x_text(self):
        html = etree.HTML(self.text)
        result = etree.tostring(html)
        print(result.decode('utf-8'))
    def x_file(self):
        html = etree.parse('./test.html', etree.HTMLParser())
        result = etree.tostring(html)
        print(result.decode('utf-8'))
    # 获取所有节点
    def x_allnodes(self):
        html = etree.parse(self.filename, etree.HTMLParser())
        result = html.xpath('//*')
        print(result)

        node = html.xpath('//li["@item-0"]')
        print(node)

    def x_test(self):
        html = etree.parse(self.filename, etree.HTMLParser())
        result = html.xpath('//a[@href="link4.html"]/../@class')
        print(result)

    def x_fathernode(self):
        html = etree.parse(self.filename, etree.HTMLParser())
        # 查找href为link4.html的a标签的父节点的class属性
        result = html.xpath('//a[@href="link4.html"]/../@class')
        print(result)

        ## 方式2
        from lxml import etree
        html = etree.parse(self.filename, etree.HTMLParser())
        result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
        print(result)
    def x_subnode(self):
        html = etree.parse(self.filename, etree.HTMLParser())
        result = html.xpath('//li/a')
        print(result)
    # 属性匹配
    def x_attr(self):
        html = etree.parse(self.filename, etree.HTMLParser())
        result = html.xpath('//li[@class="item-0"]')
        print(result)
    # 文本获取
    def x_gettext(self):
        ## 方式一：找到对应字标签，提取文本，比较整齐
        ## 方式二：直接用//text(),会有一些换行等特殊字符
        html = etree.parse(self.filename, etree.HTMLParser())
        result = html.xpath('//li[@class="item-0"]/a/text()')
        print(result)
        # 另一种方式，选取所有li标签下的文本，包括自己的和子标签的
        html = etree.parse(self.filename, etree.HTMLParser())
        result = html.xpath('//li[@class="item-0"]//text()')
        print(result)
    def x_getattr(self):
        html = etree.parse(self.filename, etree.HTMLParser())
        result = html.xpath('//li/a/@href')
        print(result)
    # 属性多值匹配
    # 有时候属性会有多个值，比如
    # <li class="li li-first"><a href="link.html">first item</a></li>
    # 这时就需要用 contains 方法了，代码可以改写如下：
    def x_getattrs(self):
        text = '''  
        <li class="li li-first"><a href="link.html">first item</a></li>  
        '''
        html = etree.HTML(text)
        result = html.xpath('//li[contains(@class, "li")]/a/text()')
        print(result)

    # 多属性匹配
    # 我们可能还遇到一种情况，那就是根据多个属性确定一个节点，
    # 这时就需要同时匹配多个属性。此时可以使用运算符 and 来连接，示例如下：
    def x_multiattr(self):
        text = '''  
        <li class="li li-first" name="item"><a href="link.html">first item</a></li>
        '''
        html = etree.HTML(text)
        result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
        print(result)
    # 按序选择
    def x_order(self):
        text = '''
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
        '''
        html = etree.HTML(text)
        result = html.xpath('//li[1]/a/text()')
        print(result)
        result = html.xpath('//li[last()]/a/text()')
        print(result)
        result = html.xpath('//li[position()<3]/a/text()')
        print(result)
        result = html.xpath('//li[last()-2]/a/text()')
        print(result)
    def x_axis(self):
        text = '''
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
        '''
        html = etree.HTML(text)
        result = html.xpath('//li[1]/ancestor::*')
        print(result)
        result = html.xpath('//li[1]/ancestor::div')
        print(result)
        result = html.xpath('//li[1]/attribute::*')
        print(result)
        result = html.xpath('//li[1]/child::a[@href="link1.html"]')
        print(result)
        result = html.xpath('//li[1]/descendant::span')
        print(result)
        result = html.xpath('//li[1]/following::*[2]')
        print(result)
        result = html.xpath('//li[1]/following-sibling::*')
        print(result)




x = model()
x.x_order()