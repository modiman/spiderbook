import requests
from requests.packages import urllib3
# use of requests
class model:
    def __init__(self):
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
                      'Cookie':'_zap=16b08aa2-7986-4803-aa6e-ce0006e15b7b; d_c0="AHBfQIk9DxOPTr2KIluPL79QV5yVxb_IzrY=|1620220278"; __snaker__id=CzDOV6rg5g6BBLGu; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=AoYmASRyOmVERVURAFcq01uwr12PrbtX;',
                      'Host':'www.zhihu.com'
}
    def request_type(self):
        r = requests.post('http://httpbin.org/post')
        r = requests.put('http://httpbin.org/put')
        r = requests.delete('http://httpbin.org/delete')
        r = requests.head('http://httpbin.org/get')
        r = requests.options('http://httpbin.org/get')

    # 带参 get
    def get_params(self):
        data = {
            'name': 'germey',
            'age': 22
        }
        r = requests.get("http://httpbin.org/get", params=data)
        print(r.text)
        return r.text
    # 解析返回值
    '''
    get函数默认返回字符串
    使用json()函数可将json型返回值解析为字典（非json型数据会报错）
    '''
    def json_parse(self):
        r = requests.get("http://httpbin.org/get")
        print(type(r.text))
        print(r.json())
        print(type(r.json()))
    # 抓取二进制
    def get_binary(self,url):
        r = requests.get(url)
        '''
        查看r内容
        print(r.text)
        print(r.content)
        '''
        # 下载图片，wb表示以二进制形式打开文件，还可以向文件写入数据
        with open('favicon.ico', 'wb') as f:
            f.write(r.content)
    # POST请求
    def post_data(self):
        data = {'name': 'germey', 'age': '22'}
        r = requests.post("http://httpbin.org/post", data=data)
        print(r.text)
    def response_data(self):
        r = requests.get('http://www.jianshu.com')
        print(type(r.status_code), r.status_code)
        print(type(r.headers), r.headers)
        print(type(r.cookies), r.cookies)
        print(type(r.url), r.url)
        print(type(r.history), r.history)
    # 高级功能
    # 文件上传
    def upload_file(self):
        files = {'file': open('favicon.ico', 'rb')}
        r = requests.post('http://httpbin.org/post', files=files)
        print(r.text)
    def cookies(self):
        r = requests.get('https://www.baidu.com')
        print(r.cookies)
        for key, value in r.cookies.items():
            print(key + '=' + value)
        html = requests.get('https://www.zhihu.com',headers=self.headers)
        print(html.text)
    def cookie_jar(self):
        cookies =  '_zap=16b08aa2-7986-4803-aa6e-ce0006e15b7b; d_c0="AHBfQIk9DxOPTr2KIluPL79QV5yVxb_IzrY=|1620220278"; __snaker__id=CzDOV6rg5g6BBLGu; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=AoYmASRyOmVERVURAFcq01uwr12PrbtX; _xsrf=0nrLlSG5kBfZ1v8PbevPU5t8atelGEhy; tshl=; YD00517437729195%3AWM_NI=ybb7J%2Bb0h1aTlVbqmBEG12QFB7VEMxQmvmU6%2BofakaMeMPIsGpuA2HTzYO4FpqifaG2Lzzna48l2KrMTAIzk%2BKJq01aMC5bs8vMH0XP%2BYzo3F4lr8nBp66W9qT6NVPC3SG0%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee8ac97b928f8283f5699abc8aa3c14e938b8baef834a894848cd03f96e9fcb8d62af0fea7c3b92abbbeaed8c921a2f0a8d2e460b08aae92f04a8799ffd3d44e82e99aa6d07493b3ba8ed83ee9b1aa82ea6b8fbb83b1cc7985b0bba2b14498a697b0b74eb4afa787e44df294b69bed6bf8e8a4d3ca7a8f8c8faaf961e9958692b33ba3938dd6e179fcaa83a9b35494f5979bee3986eca493bb6682b0fad7d633b38cfaafd55c81ed9da8b337e2a3; captcha_session_v2="2|1:0|10:1634711945|18:captcha_session_v2|88:YmVQd2dIbHNQa0lyVkRhZjZNS0ljaitqNnlML3M5eGxFUXZCQTlFcG1ZVkVnQXRoeGJoMDF4d3psaVVONVRhZg==|242e53487be6487f0dfad009f34a6f79582d35e3c04a4df706c718eaa390aac2"; gdxidpyhxdE=kTM4wWkPoiUw0ZXjIkjj8CaYJteJ57c%2BVk5tvD9ik%5CV%5CPJNEeow5NPxCN%2FKtl%5CScwCDpht7ckl1uUK%2BEaSb1%5ChNyX9OK%2BZGki1DnYyukil4UYvX1Sc936ZiOGgoZ3Zj3EUGme6uJ5%5C2m7ldySRQaVK7zHNPOeQu4VShh%2Fxlc5s0cljiH%3A1634712845558; r_cap_id="ODk2MzRlYjY4YmM3NDBlZWI2YTQwY2VjMGY2YzNiMWQ=|1634711949|6868bf217c0dceaef697bf34234a76289c093ed2"; cap_id="YzIyMzg1NjVhN2E3NDBkNWE5MzU0N2M4ZGI0ZjhjMzc=|1634711949|71bb298a33cf6908ab9e31f9fbb0cd666842bfc0"; l_cap_id="ZjdjN2VhNmU3YzEzNGZjYzg0YjE0OWM1MzllNGYxZjY=|1634711949|c0f00f7aa0f663b0e8f46e1530961215f2f6d73a"; z_c0=Mi4xRzlsakF3QUFBQUFBY0Y5QWlUMFBFeGNBQUFCaEFsVk4yUWRkWWdDajRzV01pWjlFREllYVZ5VUtudnZ3TGJnZ0lB|1634712025|d837780552016cd9fd56297653048ec39bfdf815; q_c1=3cc20c6d499142b5a952a70fa5d0ed08|1636339298000|1625483483000; tst=h; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1636352158,1636352195,1636352241,1636422868; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1636422868; NOT_UNREGISTER_WAITING=1; KLBRSID=031b5396d5ab406499e2ac6fe1bb1a43|1636422869|1636422494; SESSIONID=WD43mRtbXvvqdOPQ3oKux2SpFBlKu2MeHzQXlAzy2wN; JOID=UF4XAkuojm5Wl4OYV6soM4MZvZFE-85ZZPjV6Dby_Bwk8s7MAn1d5TSRg59V4J9W3mR_-iZ-rBjuPqu3F3Ub-kA=; osd=W1oVCkOjimxen4icVaMgOIcbtZlP_8xRbPPR6j769xgm-sbHBn9V7T-VgZdd65tU1mx0_iR2pBPqPKO_HHEZ8kg='
        jar = requests.cookies.RequestsCookieJar()
        headers = {
            'Host': 'www.zhihu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
        }
        for cookie in cookies.split(';'):
            key, value = cookie.split('=', 1)
            jar.set(key, value)
        r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
        print(r.text)

    def session(self):
        import requests
        s = requests.Session()
        s.get('http://httpbin.org/cookies/set/number/123456789')
        r = s.get('http://httpbin.org/cookies')
        print(r.text)
    def verify(self):
        response = requests.get('https://www.12306.cn')
        urllib3.disable_warnings()
        response = requests.get('https://www.12306.cn', verify=False)
        print(response.status_code)
    def set_timeout(self):
        r = requests.get('https://www.taobao.com', timeout=1)
        '''
        通过这样的方式，我们可以将超时时间设置为 1 秒，如果 1 秒内没有响应，那就抛出异常。
        实际上，请求分为两个阶段，即连接（connect）和读取（read）。
        上面设置的 timeout 将用作连接和读取这二者的 timeout 总和。
        如果要分别指定，就可以传入一个元组：
        '''
        r = requests.get('https://www.taobao.com', timeout=(5, 30))

        #永久等待
        r = requests.get('https://www.taobao.com', timeout=None)

    def auth(self):
        # 身份认证
        r = requests.get('http://localhost:5000', auth=('username', 'password'))
        print(r.status_code)


        # 另一种认证方法
        url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
        auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
                      'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
        requests.get(url, auth=auth)



if __name__ == '__main__':
    m = model()
    m.verify()