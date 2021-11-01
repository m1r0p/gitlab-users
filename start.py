#!/usr/bin/env python3
 
###### import

##### local files
from functions import *
from print_help import print_help

##### libraries
import sys

###### start 
def main():
    for opt in sys.argv:
        if opt == '--help':
            print_help()
        elif opt == '--gitver':
            versions = check_version()
            if versions[0] == versions[1]:
                print("OK")
                sys.exit(0)
            else:
                print("Cur ver = %s, Available ver = %s" % (versions[0], versions[1]))
                sys.exit(1)
        elif opt == '--gitusers':
            bad_users = check_users().get('invalid_users')
            for user in bad_users:
                if user.state == 'active':
                    print(user.username, user.email, user.state)
    


if __name__ == "__main__":
    main()

