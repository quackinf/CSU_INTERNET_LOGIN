import requests

url = "http://10.1.1.1:802/eportal/portal/login?user_account=8211211214@unicomn&user_password=qin070809"

res=requests.get(url,verify=False)
print(res._content)
