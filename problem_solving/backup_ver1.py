import os
import time

# files and directories to be backed up are specified as a list.

source = ['/User/course/notes']

# the backup must be stored in the main backup directory.

target_dir = '/User/course/backup'

target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

# it there's no folder for test:
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# run the backup
print('zip command is: ')
print(zip_command)
print('Running...please standby...')
if os.system(zip_command) == 0:
    print('Successful backup to:', target)
else:
    print('Backup failed...')
