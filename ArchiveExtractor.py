import os, errno
#Make folder for new addon
mypath = ...
if not os.path.isdir(mypath):
   os.makedirs(mypath)
#
try:
    os.makedirs(directory)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
#
os.makedirs(path, exist_ok=True)

#extract
patool
