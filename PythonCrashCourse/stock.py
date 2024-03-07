import os
import datetime
import requests

resp = requests.get("https://www.baidu.com/")
print(resp.content)
