#키워드 함수 코드

from khaiii import KhaiiiApi
api=KhaiiiApi()
sentence=input('팩트체크 검색 : ')

word=api.analyze(sentence)
keyword=[]
realkeyword=[]

for a in word:
	firststring=str(a)
	firsttuple=firststring.partition('\t')
	firstlist=list(firsttuple)
	del firstlist[0:2]
	for b in firstlist:
		secondtuple=b.partition('+')
		secondlist=list(secondtuple)
		for c in secondlist:
			if "NNG" in c:
				keyword.append(c)
			elif "NNP" in c:
				keyword.append(c)
			elif "SL" in c:
				keyword.append(c)
			elif "SN" in c:
				if "XSN" in c:
					pass
				else:
					keyword.append(c)


for a in keyword:
	firsttuple=a.partition('/')
	realkeyword.append(firsttuple[0])




#검색 코드

import pymysql

conn=pymysql.connect(host='localhost', user='gotchanews', password='', db='snudb', charset='utf8')
curs=conn.cursor()

search_list=[]

for a in realkeyword:
	sql="select server_number from factcheck where factcheck_title like '%"+a+"%'"
	curs.execute(sql)
	rows=curs.fetchall()
	for b in rows:
		search_list.append(b[0])

just_list=[]

just_list=list(set(search_list))
dic={}
for list_name in just_list:
	dic[list_name]=0

for list_count in just_list:
	dic[list_count]=dic[list_count]+1


search_result=[]
search_result=sorted(dic.items(), key=lambda t : t[1], reverse=True)

result_for_show=[]
result_for_show=search_result[:3]

realresult=[]
sql2="select factcheck_title, press, factcheck_result, factcheck_url from factcheck where server_number=%s"

for a in result_for_show:
	curs.execute(sql2%a[0])
	rows=curs.fetchall()
	for b in rows:
		realresult.append(b[0])
		realresult.append(b[1])
		realresult.append(b[2])
		realresult.append(b[3])


#결과값 표현

count=0
for a in realresult:
	count+=1
	if count%4==1:
		print(a)
	elif count%4==2:
		print("언론사 : %s"%a)
	elif count%4==3:
		print("결과 : %s"%a)
	elif count%4==0:
		print("%s/n"%a)
