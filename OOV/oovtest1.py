 # -*- encoding:UTF-8 -*-
 # oovtest1.py 最大逆向匹配
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs

#筛选oov的词典
aa=codecs.open('dict.merge.20170515.list1','r','utf-8')                
ab=aa.readlines()
lexicon=[a.replace('\n','') for a in ab]

# 分别存储oov词典大于四字词、三字词和小于等于二字词
# char1_5=[]
char1_4=[]
char1_3=[]
char1_2=[]

for c in lexicon:
	# if len(c.split('\r\n')[0])>=5:
		# char1_5.append(c.split('\r\n')[0])
	if len(c.split('\r\n')[0])>=4:
		char1_4.append(c.split('\r\n')[0])
	if len(c.split('\r\n')[0])==3:
		char1_3.append(c.split('\r\n')[0])
	if len(c.split('\r\n')[0])<=2:
		char1_2.append(c.split('\r\n')[0])

		
#char1_5=set(char1_5)		
char1_4=set(char1_4)
char1_3=set(char1_3)
char1_2=set(char1_2)


def check_indict(data):
	data1=unicode(data, errors='ignore')
	lendata=len(data1)
	# if lendata>=5:
		# if data in char1_5:
			# return True
	if lendata>=4:
		if data1 in char1_4:
			return True
	elif lendata==3:
		if data1 in char1_3:
			return True
	else:
		if data1 in char1_2:
			return True
	return False




#hmm字典
dic=codecs.open('dict.merge.20170515.list.cn1','r','utf-8')
diclines=dic.readlines()
diclines=[b.replace('\n','') for b in diclines]
dic.close()

#分别存储四字词、三字词和二字词
char_4=[]
char_3=[]
char_2=[]

for c in diclines:
    if len(c.split('\r\n')[0])==4:
        char_4.append(c.split('\r\n')[0])
    elif len(c.split('\r\n')[0])==3:
        char_3.append(c.split('\r\n')[0])
    else:
        char_2.append(c.split('\r\n')[0])

char_4=set(char_4)
char_3=set(char_3)
char_2=set(char_2)


def hmm(data):
	MAXLEN=4
	sen2=unicode(data, errors='ignore')
	length=len(sen2)
	i=length 
	temp=[]	
	while i>0:
		
		if i-MAXLEN>=0:
			possible_word=sen2[i-MAXLEN:i]
			if possible_word in char_4:
				temp.append(possible_word)
				i-=MAXLEN
				continue

		if i-3>=0:
			possible_word=sen2[i-3:i]

			if possible_word in char_3:
				temp.append(possible_word)
				i-=3
				continue

		if i-2>=0:
			possible_word=sen2[i-2:i]
			if possible_word in char_2:
				temp.append(possible_word)
				i-=2
				continue

		possible_word=sen2[i-1]
		temp.append(possible_word)
		i-=1

	temp.reverse() #将字符进行翻转
	result=' '.join(temp)
	#result=temp
	return result

	
def check_chinese(check_str):
    ch = check_str.decode('utf-8')
    if u'\u4e00' <= ch <= u'\u9fff' :
        return True
    return False	

	
# #输入文本
# #f=open('wenxue_enjoybar.ppllt500')
# #f=open('Culture_QQ.ppllt500')
# f=open('faq.chn17_final.ppllt500')
# #f=open('test3')
# sen = f.readlines()
# #输出文本
# #segResult=open('wenxue_enjoybar.ppllt500_out', 'wb')
# #segResult=open('Culture_QQ.ppllt500_out1', 'wb')
# #segResult=open('test3_out1', 'wb')
# segResult=open('faq.chn17_final.ppllt500_out1', 'wb')


	
	
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
		sen1=''.join(line)
		testsen1=sen1.split()
		length=len(testsen1)
		outresult= []
		for j in range(0,length):
			if not check_chinese(testsen1[j]):   #判断是不是中文，不是中文直接输出
				outresult.append(testsen1[j])
			else:
				if check_indict(testsen1[j]):
					outresult.append(testsen1[j])
				else:
					newoov=testsen1[j]
					newoov1=''.join(newoov)
					outresult.append(hmm(newoov1))	
		#print (' '.join(outresult))
		outresult1=' '.join(outresult)
		ff.write(outresult1+'\n')

	
ff.close()

