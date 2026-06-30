import os
import shutil
from datetime import datetime

foldernameforbackup = input("Enter the folder name to backup: ")

# Get today's date
today = datetime.now().strftime("%Y-%m-%d")

# Create backup folder name using concatenation
backupfolder = "backup_" + today

if not os.path.exists(foldernameforbackup):
    print("Folder doesn't exist.")
else:
    if not os.path.exists(backupfolder):
        os.mkdir(backupfolder)

    files = os.listdir(foldernameforbackup)

    for file in files:
        sourcePath = foldernameforbackup + "/" + file
        destinationPath = backupfolder + "/" + file

        shutil.copy(sourcePath, destinationPath)

    print("Backup completed successfully.")