'''
基于项目做定制化封装
1、鉴权:token
2、项目通用的请求头:
    {"X-Lemonban-Media-Type": "lemonban.v2"}

3、请求体格式：application/json
'''
import requests

def __handle_header(token =None):
    '''
    处理请求头，加上项目当中必带的请求头。如果有token，加上token
    :param token:
    :return:
    '''
    headers = {"X-Lemonban-Media-Type": "lemonban.v2",
               "Content-Type": "application/json"}
    if token:
        headers["Authorization"] = 'Bearer {}'.format(token)
    return headers

def send_requests(method,url,data =None,token=None):
    headers =__handle_header(token)
    method=method.upper()
    if method == "GET":
        resp =requests.get(url,params=data,headers=headers)
    elif method =="POST":
        resp =requests.post(url,json=data,headers=headers)
    return resp

if __name__ == '__main__':
    login_url = 'http://api.lemonban.com/futureloan/member/login'
    login_datas = {"mobile_phone": "18634561262", "pwd": "123456789"}
    resp_login =send_requests('post',login_url,login_datas)
    print(resp_login.json())
    token =resp_login.json()['data']['token_info']['token']
    print(token)


    recharge_url ='http://api.lemonban.com/futureloan/member/recharge'
    recharge_datas ={"member_id":1234577990,"amount":100}
    res= send_requests("post", recharge_url, recharge_datas, token)
    print(res.json())