import  requests
url = 'http://api.lemonban.com/futureloan/member/register'
data = {"mobile_phone":"18834561262","pwd":"123456789"}
headers ={'X-Lemonban-Media-Type':'lemonban.v2'}
resp = requests.post(url,json=data,headers=headers)
print(resp.status_code)
print(resp.headers)
body = resp.text
print(type(data))