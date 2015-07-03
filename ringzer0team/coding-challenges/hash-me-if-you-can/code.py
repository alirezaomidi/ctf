import requests
import hashlib
import re

url = 'http://ringzer0team.com/challenges/13'
login_url = 'http://ringzer0team.com/login'
text_regex = '----- BEGIN MESSAGE -----<br />\r\n\t\t(\w+)'
flag_regex = 'FLAG-\w+'
session = requests.session()

def get_text(username, password):
    login_data = dict(username=username, password=password)
    session.post(login_url, data=login_data)
    r = session.post(url)
    text = re.search(text_regex, r.text)
    return text.group(1)

def hash(text):
    return hashlib.sha512(text).hexdigest()

def send_answer(username, password):
    text = get_text(username, password)
    return session.post(url + '/' + str(hash(text)))

def get_flag(username, password):
    r = send_answer(username, password)
    text = re.search(flag_regex, r.text)
    if text:
        return text.group()
    else:
        return 'Error getting flag. It may took more than 2 seconds'