import os
import sys
import json
import requests


url = 'https://api.github.com/user/repos'
token = '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'
username = 'labib1235'

headers = {
  "Accept": "application/vnd.github.v3+json"
}

data = {
  "name": 'ammm',
  "private": False,
}

res = requests.post(url, data=json.dumps(data), headers=headers, auth=(username, token))
print(res.json())

ssh_uri = res.json()['ssh_url']

os.system(f'git clone {ssh_uri}')
