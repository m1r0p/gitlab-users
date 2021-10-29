#!/usr/bin/env python3
 
###### import

##### local files
from functions import *

##### libraries
import sys

###### start 
def main():
    #invalid_users = check_users().get('invalid_users')
    #for user in invalid_users:
    #    print("user = %s, email = %s state = %s" % (user.username, user.email, user.state))
    #    #print(user.email.split('@')[1])
    ver = get_version()
    print(ver)
    


if __name__ == "__main__":
    main()

