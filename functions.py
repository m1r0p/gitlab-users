#!/usr/bin/env python3
 
###### import 

##### local files
from config import (
        GITLAB_BASE_URL,
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
import paramiko

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

def check_version():
    versions = list()
    with requests.Session() as s:
        #s.auth = OAuth1(GITLAB_TOKEN) 
        resp = json.loads(requests.get(GITLAB_VERSION_URL, verify=True, headers={'PRIVATE-TOKEN': GITLAB_TOKEN}).content.decode())
        current_version = resp.get('version')

    k = paramiko.RSAKey.from_private_key_file("./gitlab.key")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect( hostname = GITLAB_BASE_URL, username = "user", pkey = k )
    c.exec_command("apt update")
    stdin, stdout, stderr = c.exec_command("apt list -a gitlab-ce | awk '{print $2}'")
    last_version = stdout.read().decode().split('\n')[1].split('-')[0]
    c.close()

    versions.append(current_version)
    versions.append(last_version)
       
    return versions


