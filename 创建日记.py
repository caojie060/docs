import os
import time
import datetime

now = datetime.datetime.now()
year = now.year
month = now.strftime('%m')
day = now.strftime('%m%d')

PATH = 'zh-cn/Dairy/'
year_path = os.path.join(PATH, str(year))
month_path = os.path.join(year_path, str(month))
day_path = os.path.join(month_path, str(day))
if not os.path.exists(year_path):
    os.makedirs(year_path)
if not os.path.exists(month_path):
    os.makedirs(month_path)
file_name = day+'.md'
file_path = day_path+'.md'
data = '# '+str(day)+'\n'
with open(file_path, mode='a', encoding='utf-8') as f:
    f.write(data)
