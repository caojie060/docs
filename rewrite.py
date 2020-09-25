import os
import re

rootdir = 'zh-cn'


def finding(rootdir, count):
    dirs = os.listdir(rootdir)
    # print('dirs:',dirs)
    pattern_r = re.compile(r'[^_].*?\.md$')

    for dir in dirs:
        fulldirpath = os.path.join(rootdir + '\\' + dir)
        # print('fulldirpath:',fulldirpath)
        target_string = re.match(pattern_r, dir)
        if os.path.isdir(fulldirpath):
            for i in range(count):
                print(' ', end='', file=wr)

            if count == 0:
                print('\n', file=wr)
                print('#', dir, file=wr)
            elif count == 2:
                print('-', dir, file=wr)
            # print('dir:',dir)
            count += 2
            finding(fulldirpath, count)
            count -= 2
        elif (count >= 2) & (target_string != None):
            for i in range(count):
                print(' ', end='', file=wr)
                pass # todo you need do something here;
            # print('dir:',dir,end='')
            dir2 = dir[0:-3] 
            print('- [', dir2, ']', end='', file=wr)
            print('(', fulldirpath, ')', file=wr)


with open('_sidebar.md', 'w', encoding='utf-8')as wr:
    finding(rootdir, 0)
