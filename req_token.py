import requests
login_url ='http://api.lemonban.com/futureloan/member/login'
login_datas ={"mobile_phone":"18634561262","pwd":"123456789"}
headers ={"X-Lemonban-Media-Type":"lemonban.v2"}
resp = requests.post(login_url,json=login_datas,headers=headers)
resp_dict = resp.json()
for key,value in resp_dict.items():
    print(key,value)

token = resp_dict['data']['token_info']['token']
print(token)

member_id = resp_dict['data']['id']
amount =120
headers["Authorization"]= 'Bearer {}'.format(token)
print(headers["Authorization"])

recharge_url ='http://api.lemonban.com/futureloan/member/recharge'
recharge_datas ={"member_id":member_id,"amount":amount}
resp2 = requests.post(recharge_url,json=recharge_datas,headers=headers)
print(resp2.json())