import re
class regex:
    def __init__(self):
        self.content = 'Hello 123 4567 World_This is a Regex Demo'
        self.html = '''<div id="songs-list">
               <h2 class="title"> 经典老歌 </h2>
               <p class="introduction">
               经典老歌列表
               </p>
               <ul id="list" class="list-group">
               <li data-view="2"> 一路上有你 </li>
               <li data-view="7">
               <a href="/2.mp3" singer="任贤齐"> 沧海一声笑 </a>
               </li>
               <li data-view="4" class="active">
               <a href="/3.mp3" singer="齐秦"> 往事随风 </a>
               </li>
               <li data-view="6"><a href="/4.mp3" singer="beyond"> 光辉岁月 </a></li>
               <li data-view="5"><a href="/5.mp3" singer="陈慧琳"> 记事本 </a></li>
               <li data-view="5">
               <a href="/6.mp3" singer="邓丽君"> 但愿人长久 </a>
               </li>
               </ul>
               </div>'''

        pass
    def re_match(self):

        print(len(self.content))
        '''
        用它来匹配这个长字符串。开头的 ^ 是匹配字符串的开头，也就是以 Hello 开头；
        然后 \s 匹配空白字符，用来匹配目标字符串的空格；
        \d 匹配数字，3 个 \d 匹配 123；
        然后再写 1 个 \s 匹配空格；
        后面还有 4567，我们其实可以依然用 4 个 \d 来匹配，但是这么写比较烦琐，
        所以后面可以跟 {4} 以代表匹配前面的规则 4 次，也就是匹配 4 个数字；
        然后后面再紧接 1 个空白字符，最后 \w{10} 匹配 10 个字母及下划线。
        我们注意到，这里其实并没有把目标字符串匹配完，不过这样依然可以进行匹配，
        只不过匹配结果短一点而已。
        而在 match 方法中，第一个参数传入了正则表达式，第二个参数传入了要匹配的字符串。
        打印输出结果，可以看到结果是 SRE_Match 对象，这证明成功匹配。
        该对象有两个方法：group 方法可以输出匹配到的内容，
        结果是 Hello 123 4567 World_This，这恰好是正则表达式规则所匹配的内容；
        span 方法可以输出匹配的范围，结果是 (0, 25)，
        这就是匹配到的结果字符串在原字符串中的位置范围。
        '''
        result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', self.content)
        print(result)
        print(result.group())
        print(result.span())
    def re_group(self):

        result = re.match('^Hello\s(\d+)\s(World)', self.content)
        '''
        这里可以使用 () 括号将想提取的子字符串括起来。
        () 实际上标记了一个子表达式的开始和结束位置，
        被标记的每个子表达式会依次对应每一个分组，
        调用 group 方法传入分组的索引即可获取提取的结果。
        示例如下：
        '''
        print(result)
        print(result.group(2))
        print(result.group(1))
        print(result.span())
    def re_general(self):
        result = re.match('^Hello.*Demo$', self.content)
        print(result)
        print(result.group())
        print(result.span())
    def re_greedy(self):

        # 贪婪匹配
        result = re.match('^He.*(\d+).*Demo$', self.content)
        '''
        这里就涉及一个贪婪匹配与非贪婪匹配的问题了。
        在贪婪匹配下，. 会匹配尽可能多的字符。
        正则表达式中. 后面是 \d+，也就是至少一个数字，
        并没有指定具体多少个数字，因此，.* 就尽可能匹配多的字符，
        这里就把 123456 匹配了，给 \d + 留下一个可满足条件的数字 7，
        最后得到的内容就只有数字 7 了
        '''

        print(result)
        print(result.group(1))
        result1 = re.match('^He.*?(\d+).*Demo$', self.content)
        print(result1.group(1))
    def test(self):
        content = 'Hello 1234567 World_This is a Regex Demo'
        print(re.match('.*(\d+).*',content).group(1))
    #转义，如果字符串本身包含. * 等特殊字符就需要转义
    def zhuanyi(self):
        content = '(百度) www.baidu.com'
        result = re.match('\(百度 \) www\.baidu\.com', content)
        print(result)

    # match只能匹配指定开头结尾的字符串
    # search到字符串中查找满足条件的子串
    def re_search(self):

        #re.S:修饰符，为了匹配结点之间的换行符
        result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', self.
                           html, re.S)
        '''
        <li：表明到li标签中查找
        .*?：以非贪婪方式匹配所有字符，直到下一个条件出现
        active：active可以匹配类
        .*?:继续通配
        singer=":
        第一个(.*?) :查找从singer="  到  ">之间的所有字符，并归入group(1)
        第二个(.*?) :查找从">  到  </a>'之间的所有字符,并归入group(2)
        
        最后总的结果应该是
        <li....active.....singer="group(1)">group(2 )</a>
        '''
        if result:
            print(result.group(1), result.group(2))
    # 如果只是获取第一个内容，可以用 search 方法。当需要提取多个内容时，可以用 findall 方法。
    def re_findall(self):
        results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', self.html, re.S)
        print(results)
        print(type(results))
        for result in results:
            print(result)
            print(result[0], result[1], result[2])
    '''
    除了使用正则表达式提取信息外，有时候还需要借助它来修改文本。
    比如，想要把一串文本中的所有数字都去掉，如果只用字符串的 replace 方法，那就太烦琐了，
    这时可以借助 sub 方法。示例如下：
    '''
    def re_sub(self):
        content = '54aK54yr5oiR54ix5L2g'
        # 删除字符串中的数字
        content = re.sub('\d+', '', content)
        print(content)
    '''
    前面所讲的方法都是用来处理字符串的方法，最后再介绍一下 compile 方法，
    这个方法可以将正则字符串编译成正则表达式对象，以便在后面的匹配中复用。示例代码如下：
    '''
    def re_compile(self):
        content1 = '2016-12-15 12:00'
        content2 = '2016-12-17 12:55'
        content3 = '2016-12-22 13:21'
        pattern = re.compile('\d{2}:\d{2}')
        result1 = re.sub(pattern, '', content1)
        result2 = re.sub(pattern, '', content2)
        result3 = re.sub(pattern, '', content3)
        print(result1, result2, result3)


if __name__ == '__main__':
    r = regex()
    r.re_compile()
