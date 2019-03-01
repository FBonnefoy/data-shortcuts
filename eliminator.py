import os
path = input('SVP introduire directoire du travail:\n')
if len(path)<1:
	os.chdir('C:\\Users\\f.bonnefoy\\Desktop\\Brands')
else:
	os.chdir(path)
fname=input("file name of list?\n")
fhandle=open(fname)
list=[]
for line in fhandle:
	word=line.strip()
	word=str(word)
	if word not in list:
		list.append(word)
str1 = ','.join(str(e) for e in list)
str1 = str1.replace("'",'')
str1 = str1.replace("[",'')
str1 = str1.replace("]",'')
print(list)
print(str1)
rlist=str.split(',')
vlist=[]
fname2=input("file name of inputs?\n")
fhandle2=open(fname2)
ofname=input("name of output")
of=open(ofname,"w+")
for line in fhandle2:
	word2=line.strip()
	if word not in list:
		vlist.append("yes")
		of.write("yes\n")
	else:
		vlist.append("no")
		of.write("no\n")
of.close()
for i in vlist:
	print(i)
str2 = ','.join(str(e) for e in list)
str2 = str2.replace("'",'')
str2 = str2.replace("[",'')
str2 = str2.replace("]",'')
cont=input('continue?\n')
if len(cont)<1:
	sys.exit()
else:
	outfile=input("name of output")
	brandput = open(outfile,"w")
	brandput.write(str2)
	brandput.close()
