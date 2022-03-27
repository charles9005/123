import requests
s =requests.Session()
print("登录前的数据",s.cookies)
login_url = "https://www.ketangpai.com/UserApi/login"
login_datas = {"email":"18259275639","password":"lin123","remember":0}
response = s.post(login_url,data=login_datas)
print(response.cookies)
print(s.cookies)
requests.get()


