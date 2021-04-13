import os
import re
import shutil
import datetime
now = datetime.datetime.now()
year = now.year
PATH = 'zh-cn/Dairy/'
year_path=os.path.join(PATH,str(year))
list_dir=os.walk(PATH)
# for root,dirs,files in list_dir:
#     for file in files:
#         print(file)
for dir in os.listdir(PATH):
    dir_path=os.path.join(PATH,dir)
    if os.path.isfile(dir_path):
        print(dir)
        month=dir[:2]
        print(month)
        month_path=os.path.join(year_path,month)
        target_path=os.path.join(month_path,dir)
        if not os.path.exists(target_path):
            shutil.move(dir_path,month_path)
        else:
            data='\n'
            with open(dir_path,encoding='utf-8')as fr:
                data+=fr.read()
            data+='\n'
            with open(target_path,mode='a',encoding='utf-8') as fw:
                fw.write(data)
            os.remove(dir_path)