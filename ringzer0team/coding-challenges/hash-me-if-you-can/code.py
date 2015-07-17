import requests
import hashlib
import re
import getpass

url = 'http://ringzer0team.com/challenges/13'
login_url = 'http://ringzer0team.com/login'
text_regex = '----- BEGIN MESSAGE -----<br />\r\n\t\t(\w+)'
flag_regex = 'FLAG-\w+'
wrong_regex = 'Wrong.*!'
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
    flag = re.search(flag_regex, r.text)
    wrong = re.search(wrong_regex, r.text)
    if flag:
        return flag.group()
    elif wrong:
        return wrong.group()
    else:
        return 'Unknown Error!'

if __name__ == '__main__':
    username = raw_input('Enter your ringzer0team username: ')
    password = getpass.getpass('Enter your ringzer0team password: ')
    try:
        print get_flag(username, password)
    except (requests.exceptions.RequestException, AttributeError) as e:
        print 'Connection Error!'
