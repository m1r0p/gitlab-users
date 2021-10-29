#!/usr/bin/env python3
 
###### import
##### constants

##### functions
from functions import *

###### start 
def main():
    users = get_users_from_gitlab()
    i = 0
    for user in users:
        i = i + 1

    print(i)

if __name__ == "__main__":
    main()

