import os
import re

rootdir = 'zh-cn'


def finding(rootdir, count):
    dirs = os.listdir(rootdir)
    # print('dirs:',dirs)
    pattern_r = re.compile(r'[^_].*?\.md$')
    # pattern_r = re.compile(r'[^_].*?\.*$')

    for dir in dirs:
        if dir.startswith('.'):
            continue
        full_path = os.path.join(rootdir + '/' + dir)
        # print('full_path:',full_path)
        target_string = re.match(pattern_r, dir)
        if os.path.isdir(full_path):
            for i in range(count):
                print(' ', end='', file=wr)
            print('- '+dir, file=wr)
            # print('dir:',dir)
            count += 2
            finding(full_path, count)
            count -= 2
        elif (count >= 2) & (target_string != None):
            for i in range(count):
                print(' ', end='', file=wr)
            # print('dir:',dir,end='')
            file_name = dir[0:-3]
            print('- ['+file_name+']', end='', file=wr)
            full_path = full_path.replace(' ', '%20')
            print('('+full_path+')', file=wr)


with open('_sidebar.md', 'w', encoding='utf-8')as wr:
    finding(rootdir, 0)
