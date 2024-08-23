import os
from sys import argv

dat=open(os.path.expanduser('~/custom_launcher.csv')).read().split('\n')
if len(argv)<2:
    for c in dat:
        if c:
            print(f'c {c.split('|')[0]}')
    exit()

for c in dat:
    if c.startswith(argv[1]+'|'):
        os.system(f'code "{c.split('|',1)[1]}" &')