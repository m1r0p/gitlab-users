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
            versions = check_git_version()
            if versions[0] == versions[1]:
                print("version %s is latest" % versions[1])
                sys.exit(0)
            else:
                print("Cur ver = %s, Available ver = %s" % (versions[0], versions[1]))
                sys.exit(2)
        elif opt == '--gitusers':
            bad_users = list()
            invalid_users = check_git_users().get('invalid_users')
            if invalid_users != []:
                for user in invalid_users:
                    bad_users.append(user.email)
                print("Rogue users: %s" % bad_users)
                sys.exit(2)
            else:
                print("There are no rogue users")
                sys.exit(0)
        elif opt == '--squashver':
            #print("feature under construction")
            check_squash_version()
    


if __name__ == "__main__":
    main()

