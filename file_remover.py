# file_remover.py
import os, sys

if len(sys.argv) == 3:
    extension   = sys.argv[1]
    dir_path    = sys.argv[2]
else:
    print("Please Enter The Extension Of Folders And The Path")
    exit()



if not os.path.isabs(dir_path):
    dir_path    = os.path.abspath(dir_path)

if not os.path.isdir(dir_path):
    print("File Doesn't Exist")
    exit()

os.chdir(dir_path)
files   = list(filter(lambda filename: filename.endswith(extension), os.listdir()))

print("Deleting Files : ")
for file in files:
    print(f"\tDeleting {file}")
    os.remove(file)

print('Done !')
