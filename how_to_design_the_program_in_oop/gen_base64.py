#!/usr/bin/python
# -*- coding: UTF-8 -*-
import base64
import getopt
import sys

# image_files = {"Evaluation Matrix Diagram.png", "General Marble Diagram.png"}

def encode_base64(file_lists):
    for image_file in file_lists:
        f=open(image_file,'rb') #二进制方式打开图文件
        ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
        f.close()

        base64_file=image_file + '.base64'
        print '%s:' % (base64_file)
        
        fbase64=open(base64_file, 'wb')
        fbase64.write("[]:data:image/png;base64,")
        fbase64.seek(0,2)
        fbase64.write(ls_f)
        fbase64.flush()
        fbase64.close()

if __name__ == "__main__":
    print 'argv:%s' % (sys.argv[1:])
    encode_base64(sys.argv[1:])
    pass
        

