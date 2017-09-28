import os
import time
import datetime

backupDIR = '/home/vagrant/newbackup/'
datetime = time.strftime('%m%d%Y-%H%M%S')
datetimeBackupDir = backupDIR + datetime
os.system("mysqldump -u root -predhat -h localhost Database1 > "+datetimeBackupDir+"Database1back.sql")







