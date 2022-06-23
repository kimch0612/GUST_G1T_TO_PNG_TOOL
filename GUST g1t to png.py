import os
import time
import shutil
from wand import image

path = '/GUST'
file_list = os.listdir(path)

a = len(file_list)
b = 0

for b in range(a):
    print(file_list[b])
    os.system('gust_g1t.exe C:\GUST\\' + file_list[b])
    time.sleep(1)
    file_list[b] = file_list[b].replace('.g1t', '')
    os.rename('C:\\GUST\\' + file_list[b] + '\\000.dds', 'C:\\GUST\\' + file_list[b] + '\\' + file_list[b] + '.dds')
    os.system('move C:\\GUST\\' + file_list[b] + '\\' + file_list[b] + '.dds C:\\GUST\\')
    shutil.rmtree('C:\\GUST\\' + file_list[b])
    os.remove('C:\GUST\\' + file_list[b] + '.g1t')
    with image.Image(filename='C:\\GUST\\' + file_list[b] + '.dds') as img:
        img.compression = "no"
        img.save(filename='C:\\GUST\\' + file_list[b] + '.png')
        os.remove('C:\GUST\\' + file_list[b] + '.dds')
    b += 1

