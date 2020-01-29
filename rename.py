import os
from pathlib import Path

# path = Path('/home/dle/TutVids/Comlete_React_Web_with_Redux')
path = Path(input('Root Path to all videos: '))
print("Folders will be given leading zeros automatically.")
print("Currently only MP4 Files will be renamed.")
print('Renaming Videos and folders to contain leading zeros.')
for r, dirs, files in os.walk(path, topdown=True):
    for file in files:
        if str(file).endswith('.mp4'):
            p = str(file).split(".")[0]
            try:
                f = int(p)
                if f < 10 and len(p) < 2:
                    old_path = Path(r) / Path(file)
                    new_path = Path(r) / Path("0" + file)
                    print(old_path)
                    print(new_path)
                    os.rename(old_path, new_path)
            except ValueError:
                print("{}: Not a Number".format(p))

    for d in dirs:
        if "." in str(d):
            p = str(d).split(".")[0]
            try:
                f = int(p)
                if f < 10 and len(p) < 2:
                    old_path = Path(r) / Path(d)
                    new_path = Path(r) / Path("0" + d)
                    print(old_path)
                    print(new_path)
                    os.rename(old_path, new_path)
            except ValueError:
                print("{}: Not a Number".format(p))

print('All done!')
