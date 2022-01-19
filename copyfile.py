import os
from shutil import copy
needs = []
with open('nacc.txt', 'r') as f:
    needs = set([s.strip() for s in f.readlines()])

os.chdir('./dicom')
files = os.listdir()
for i in files:
    if i in needs:
        copy(i, '../selected/.')
        needs.remove(i)

with open('../missing.txt', 'w') as f:
    for i in needs:
        f.write(i+'\n')
os.chdir('../')
