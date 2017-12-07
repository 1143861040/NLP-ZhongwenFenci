# -*- encoding:UTF-8 -*-
from __future__ import print_function, unicode_literals
import json
import requests
import sys
import thulac
reload(sys)
import sys, getopt

sys.setdefaultencoding('utf8')
def check_chinese(check_str): #检查是否含有中文
    ch = check_str.decode('utf-8')
    if u'\u4e00' <= ch <= u'\u9fff' :
        return True
    return False

if __name__ == "__main__":
	
	if len(sys.argv)<4:
		print("Please input the Infile and Outfile")
		sys.exit()
	for i in range(len(sys.argv)):
		if sys.argv[i]=='-i':
			input_file=sys.argv[i+1]
		elif sys.argv[i]=='-o':
			output_file=sys.argv[i+1]
	f=open(input_file)
	ff=open(output_file,'w')
	s=f.readlines()
	for line in s:
		textdata=unicode(line, errors='ignore') #将string类型字符串变成一个unicode对象list格式
		textdata1=''.join(textdata) #？
		for i in range(0,len(textdata)):
			if i < len(textdata)-1:
				if textdata[i].isspace(): #检查字符串是否只有空格
					if check_chinese(textdata[i-1]) and check_chinese(textdata[i+1]):
						textdata=textdata[ :i]+textdata[i+1: ]
		#thu1 = thulac.thulac(seg_only=True)
        #text = thu1.cut(textdata, text=True)
		ff.write(textdata)
ff.close()
