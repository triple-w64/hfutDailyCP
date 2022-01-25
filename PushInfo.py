from requests import get, post
import json

default_headers = {
    'Content-Type': 'application/json'
}


def push_info(token, msg):
    url = 'http://pushplus.hxtrip.com/send'
    data = {
        'token': token,
        'content': msg
    }
    body = json.dumps(data).encode(encoding='utf-8')
    res = post(url, data=body, headers=default_headers)
    return res.status_code == 200
