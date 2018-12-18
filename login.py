import unittest
import requests



r = requests.post(' http://bigdata.stargraph.cn/api/user/login',data={'username':'corre','password':'kJu1mhYzmgY='})

print(r.cookies)