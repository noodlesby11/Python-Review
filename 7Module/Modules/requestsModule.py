#Python requests 是一个常用的 HTTP 请求库，可以方便地向网站发送 HTTP 请求，并获取响应结果
import requests
url = 'https://www.baidu.com/'
#打开网址,获取对象
resp=requests.get(url)
#设置编码格式
resp.encoding = 'utf-8'
print(resp.text)
