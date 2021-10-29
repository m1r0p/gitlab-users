#!/usr/bin/env python3
 
###### import 

##### local files
from config import (
        GITLAB_USERS_URL,
        AMOUNT_OF_PAGES,
        GITLAB_TOKEN,
        DEVX_DOMAINS,
        GITLAB_VERSION_URL,

)

from classes import *

##### libraries
import requests
import json

###### functions
def gen_urls():
    urls = list()
    for page in range(1, AMOUNT_OF_PAGES+1):
        urls.append(GITLAB_USERS_URL + str(page))

    return urls

def get_users_from_gitlab():
    users = list()
    urls = gen_urls()
    with requests.Session() as s:
        #s.auth = OAuth1(GITLAB_TOKEN) 
        for url in urls:
            resp = json.loads(requests.get(url, verify=True, headers={'PRIVATE-TOKEN': GITLAB_TOKEN}).content.decode())
            for user in resp:
                uid = user.get('id')
                username = user.get('username')
                state = user.get('state')
                email = user.get('email')
                globals()['%s' % uid] = User(int(uid), username, state, email)
                users.append(globals()['%s' % uid])

    return users

def check_users():
    user_list = get_users_from_gitlab()
    valid_users = list()
    invalid_users = list()
    for user in user_list:
        domain = user.email.split('@')[1]
        if domain in DEVX_DOMAINS:
            valid_users.append(user)
        else:
            invalid_users.append(user)

    users = dict()
    users['valid_users'] = valid_users
    users['invalid_users'] = invalid_users
   
    return users

def get_version():
    with requests.Session() as s:
        #s.auth = OAuth1(GITLAB_TOKEN) 
        resp = json.loads(requests.get(GITLAB_VERSION_URL, verify=True, headers={'PRIVATE-TOKEN': GITLAB_TOKEN}).content.decode())
        
    return resp.get('version')

