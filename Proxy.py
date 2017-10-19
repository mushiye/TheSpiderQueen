# encoding = utf-8
import requests

if __name__ == "__main__":
    # 访问网址，测试自己的IP是多少
    url = 'http://www.whatismyip.com.tw/'
    #  User Agent
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

    # 代理IP
    proxies = {
        "http": "http://111.200.58.94:80",
        # "https": "http://10.10.1.10:1080",
    }
    
    req = requests.get(url = url, headers = head, proxies = proxies)
    html = req.text
    print(html)