#!/usr/bin/env python3
 
###### import 

##### local files
from config import (
        GITLAB_USERS_URL,
        AMOUNT_OF_PAGES,
        GITLAB_TOKEN,

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
            resp = json.loads(requests.get(url, verify=False, headers={'PRIVATE-TOKEN': GITLAB_TOKEN}).content.decode())
            for user in resp:
                uid = user.get('id')
                username = user.get('username')
                email = user.get('email')
                globals()['%s' % uid] = User(int(uid), username, email)
                users.append(globals()['%s' % uid])

    return users

def get_valid_users(user_list):
    pass

def get_invalid_users(user_list):
    pass


