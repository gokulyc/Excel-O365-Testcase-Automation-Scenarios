import os
import time

from datetime import datetime, timedelta, timezone
# print(os.scandir())
# # print(os.listxattr())
# time.
with os.scandir() as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name,':',os.path.getsize(entry.path),':',datetime.fromtimestamp(os.stat(entry.path).st_mtime))
            
            # time.strftime('%m/%d/%Y %H:%M:%S',time.gmtime(os.path.getctime(entry.path)/1000)))