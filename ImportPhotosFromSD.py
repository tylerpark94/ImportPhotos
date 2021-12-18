#!/usr/bin/env python3

'''
Import photos from SD card into year folder and name subfolder, seperating .CR2 and .JPG
Add script to to path
'''

import os
import sys
import shutil
from datetime import datetime

# Insert appropriate path and files extention.
sd_photo_folder = '' # example: '/media/mycard/disk/DCIM/'
base_folder = '' # example: /home/Pictures
raw_extension = '.CR2'
jpg_extension = '.JPG'

# Print iterations progress
# From this SO answer: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console/15862022
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

today = datetime.now()
year_folder = str(today.year)

print ("Photos will be saved to " , base_folder,"\\",year_folder)
folder_name = input("Enter name of subfolder: ")

folder_name = folder_name.strip()

output_folder = os.path.join(base_folder, year_folder, folder_name)
raw_output_folder = os.path.join(base_folder, year_folder, folder_name, 'RAW')
jpg_output_folder = os.path.join(base_folder, year_folder, folder_name, 'JPG')

#Create output folder
try:
    os.makedirs(output_folder)
except FileExistsError as exists:
    print('Folder exists:', exists.filename)
    print('Using existing folder...')

sd_files = os.listdir(sd_photo_folder)
#Filter for raw extension
raw_files = [k for k in sd_files if k.endswith(raw_extension)]
jpg_files = [k for k in sd_files if k.endswith(jpg_extension)]

#Copy files
#Progress bar
n_files = len(raw_files) + len(jpg_files)

print('Copying', n_files, ' files')

printProgressBar(0, n_files, prefix = 'Copying photos:', suffix = '', length = 50)

if len(raw_files) > 0 :
    try:
        os.makedirs(raw_output_folder)
    except FileExistsError as exists:
        print('Folder exists:', exists.filename)
        print('Using existing folder...')

    for i, file_name in enumerate(raw_files):
        printProgressBar(i + 1, len(raw_files), prefix = 'RAW Progress:', suffix = '', length = 50)

        try:
            shutil.copy(os.path.join(sd_photo_folder, file_name), raw_output_folder)
        except Error as err:
            print(err)

if len(jpg_files) > 0 :
    try:
        os.makedirs(jpg_output_folder)
    except FileExistsError as exists:
        print('Folder exists:', exists.filename)
        print('Using existing folder...')

    for i, file_name in enumerate(jpg_files):
        printProgressBar(i + 1, len(jpg_files), prefix = 'JPG Progress:', suffix = '', length = 50)

        try:
            shutil.copy(os.path.join(sd_photo_folder, file_name), jpg_output_folder)
        except Error as err:
            print(err)


print('Finished!')
