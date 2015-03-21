#! /usr/bin/python3

import os, tarfile
from datetime import date

def main():
    Today = date.isoformat(date.today())    # store date as string
    ball = tarfile.open(Today+'_backup', 'w:bz2')   # tarball
    confPath = 'backup.config'
#    confPath = '/etc/backup.config'         # path to config file
    with open(confPath) as backConf:        # open file object to read
        for line in backConf:           # read each line in file
            filePath = line.strip()         # strips newline 
            print("adding ", filePath)      # prints pathname
            ball.add(filePath,arcname=os.path.basename(filePath))
        backConf.close()                        # close file

main() # execute main
# end of program

