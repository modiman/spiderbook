import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class model:
    def __init__(self):
        #声明一个浏览器对象，方便后续使用
        path ='E:\安装包\chromedriver_win32\chromedriver.exe'
        self.browser = webdriver.Chrome(executable_path=path)
        '''
        类似的还可以
        browser = webdriver.Chrome()
        browser = webdriver.Firefox()
        browser = webdriver.Edge()
        browser = webdriver.PhantomJS()
        browser = webdriver.Safari()
        '''

    def hello(self,browser):
        try:
            # 打开搜索引擎
            browser.get('https://www.baidu.com')
            # browser.get('https://www.google.com')
            ## 找到id为kw的标签（即输入框）
            input = browser.find_element_by_id('kw')
            # 发送关键字 Python
            input.send_keys('Python')
            # 点击确认
            input.send_keys(Keys.ENTER)
            wait = WebDriverWait(browser, 10)
            wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
            print(browser.current_url)
            print(browser.get_cookies())
            print(browser.page_source)
        finally:
            # browser.close() # 加上这句话会退出浏览器
            pass
    def visit_page(self):
        self.browser.get('http://lgn.bjut.edu.cn')
        print(self.browser.page_source)
    def find_node(self,browser):
        # browser = webdriver.Chrome()
        browser.get('https://www.taobao.com')
        # 找到id为q的标签（即输入框）
        input_first = browser.find_element_by_id('q')
        # input_first.send_keys('娃哈哈')
        # input_first.send_keys(Keys.ENTER)
        input_second = browser.find_element_by_css_selector('#q')
        input_third = browser.find_element_by_xpath('//*[@id="q"]')
        # 从输出结果可知三种方式查找的节点是完全相同的
        print(input_first,'\n', input_second, '\n',input_third)

        '''
        获取单个节点的方法包括
        find_element_by_id
        find_element_by_name
        find_element_by_xpath
        find_element_by_link_text
        find_element_by_partial_link_text
        find_element_by_tag_name
        find_element_by_class_name
        find_element_by_css_selector
        另外，Selenium 还提供了通用方法 find_element()，
        它需要传入两个参数：查找方式 By 和值。
        实际上，它就是 find_element_by_id() 
        这种方法的通用函数版本，比如 find_element_by_id(id) 
        就等价于 find_element(By.ID, id)，
        二者得到的结果完全一致。我们用代码实现一下：
        '''
        input_forth = browser.find_element(By.ID, 'q')
        print(input_forth)
        browser.close()
    def multinodes(self,browser):
        # 获取淘宝侧边栏
        browser.get('https://www.google.com')
        lis = browser.find_elements_by_css_selector('.service-bd li')
        for li in lis:
            print(li.get_property('href'),li.get_attribute('href'),li.find_element_by_tag_name('a'))
            print(li.text)
        browser.close()
    '''
    Selenium 可以驱动浏览器来执行一些操作，也就是说可以让浏览器模拟执行一些动作。
    比较常见的用法有：输入文字时用 send_keys 方法，清空文字时用 clear 方法，
    点击按钮时用 click 方法。示例如下：
    '''
    def node_inte(self):
        browser = webdriver.Chrome()
        browser.get('https://www.taobao.com')
        input = browser.find_element_by_id('q')
        input.send_keys('iPhone')
        time.sleep(1)
        input.clear()
        input.send_keys('iPad')
        button = browser.find_element_by_class_name('btn-search')
        button.click()
        browser.close()
    '''
    在上面的实例中，一些交互动作都是针对某个节点执行的。
    比如，对于输入框，我们就调用它的输入文字和清空文字方法；
    对于按钮，就调用它的点击方法。
    其实，还有另外一些操作，它们没有特定的执行对象，比如鼠标拖曳、键盘按键等，
    这些动作用另一种方式来执行，那就是动作链。
    比如，现在实现一个节点的拖曳操作，将某个节点从一处拖曳到另外一处，可以这样实现：
    '''
    def action_link(self):
        browser = webdriver.Chrome()
        url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
        browser.get(url)
        browser.switch_to.frame('iframeResult')
        source = browser.find_element_by_css_selector('#draggable')
        target = browser.find_element_by_css_selector('#droppable')
        actions = ActionChains(browser)
        actions.drag_and_drop(source, target)
        actions.perform()
    def exe_js(self):
        browser = webdriver.Chrome()
        browser.get('https://www.zhihu.com/explore')
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)
        browser.execute_script('alert("To Bottom")')
    def node_info(self):

        url = 'https://www.zhihu.com/explore'
        self.browser.get(url)
        #  找到id为js-clientConfig的结点
        logo = self.browser.find_element_by_id('js-clientConfig')
        print(logo)
        # 输出其type属性值
        print(logo.get_attribute('type'))

        # 获取文本值
        input = self.browser.find_element_by_class_name('ExploreHomePage-specialsLoginTitle')
        print(input.text)

        # 获取 ID、位置、标签名、大小
        print(input.id)
        print(input.location)
        print(input.tag_name)
        print(input.size)
        self.browser.close()
    # 10. 切换 Frame
    '''
        我们知道网页中有一种节点叫作 iframe，也就是子 Frame，相当于页面的子页面，它的结构和外部网页的结构完全一致。Selenium 打开页面后，它默认是在父级 Frame 里面操作，而此时如果页面中还有子 Frame，它是不能获取到子 Frame 里面的节点的。这时就需要使用 switch_to.frame() 方法来切换 Frame。示例如下
    '''
    def switch_frame(self,browser):
        url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
        browser.get(url)
        browser.switch_to.frame('iframeResult')
        try:
            logo = browser.find_element_by_class_name('logo')
        except NoSuchElementException:
            print('NO LOGO')
        browser.switch_to.parent_frame()
        logo = browser.find_element_by_class_name('logo')
        print(logo)
        print(logo.text)
        self.browser.close()

    # 11. 延时等待
    '''
    在 Selenium 中，get() 方法会在网页框架加载结束后结束执行，
    此时如果获取 page_source，可能并不是浏览器完全加载完成的页面，
    如果某些页面有额外的 Ajax 请求，我们在网页源代码中也不一定能成功获取到。
    所以，这里需要延时等待一定时间，确保节点已经加载出来。
    这里等待的方式有两种：一种是隐式等待，一种是显式等待。
    '''
    def delay(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.get('https://www.zhihu.com/explore')
        input = browser.find_element_by_class_name('zu-top-add-question')
        print(input)

        # 显示等待
        wait = WebDriverWait(browser, 10)
        input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
        print(input, button)
    # 12. 前进后退
    '''
    平常使用浏览器时都有前进和后退功能，Selenium 也可以完成这个操作，它使用 back() 方法后退，使用 forward() 方法前进。示例如下：
    '''
    def back(self):
        browser = webdriver.Chrome()
        browser.get('https://www.baidu.com/')
        browser.get('https://www.taobao.com/')
        browser.get('https://www.python.org/')
        browser.back()
        time.sleep(1)
        browser.forward()
        browser.close()
    # 13. Cookies使用 Selenium，还可以方便地对 Cookies 进行操作，例如获取、添加、删除 Cookies 等。示例如下：
    def set_cookies(self):
        browser = webdriver.Chrome()
        browser.get('https://www.zhihu.com/explore')
        print(browser.get_cookies())
        browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
        print(browser.get_cookies())
        browser.delete_all_cookies()
        print(browser.get_cookies())
        browser.close()
    # 14. 选项卡管理
    def opitons(self):
        browser = webdriver.Chrome()
        browser.get('https://www.baidu.com')
        browser.execute_script('window.open()')
        print(browser.window_handles)
        browser.switch_to_window(browser.window_handles[1])
        browser.get('https://www.taobao.com')
        time.sleep(1)
        browser.switch_to_window(browser.window_handles[0])
        browser.get('https://python.org')

    # 15.    异常处理
    '''
    在使用 Selenium 的过程中，难免会遇到一些异常，例如超时、节点未找到等错误，一旦出现此类错误，程序便不会继续运行了。这里我们可以使用 try except 语句来捕获各种异常。
首先，演示一下节点未找到的异常，示例如下：
    '''
    def execeptions(self):
        browser = webdriver.Chrome()
        try:
            browser.get('https://www.baidu.com')
        except TimeoutException:
            print('Time Out')
        try:
            browser.find_element_by_id('hello')
        except NoSuchElementException:
            print('No Element')
        finally:
            browser.close()




if __name__ == '__main__':
    s = model()
    s.multinodes(s.browser)
