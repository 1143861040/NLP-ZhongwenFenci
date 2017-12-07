# -*- encoding:UTF-8 -*-
from __future__ import print_function, unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba
jieba.load_userdict("dict_new")#加载自定义词典
import jieba.posseg as pseg  #词性标注
	
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
	sen=f.readlines()
	for line in sen:
		sen1=unicode(line, errors='ignore')
		sen2=''.join(sen1)#?	
 	  words = jieba.cut(sen2)
		res=' '.join(words)
		res1=res.replace("   "," ")#?		
    ff.write(res1)
		
ff.close()
