import os
cwd = os.getcwd()
cwd
fname="listecharles.txt"
fhandle=open(fname)
list=[]
for line in fhandle:
	word=line.strip()
	word=str(word)
	if word not in list:
		list.append(word)
print(list)
fhandle.close()
fname2="acorriger.txt"
fhandle2=open(fname2)
vlist=[]
for line in fhandle2:
	word=line.strip()
	word=str(word)
	if word not in vlist:
		vlist.append(word)
print(vlist)
rlist=[]
ofname="shit.txt"
of=open(ofname,"w+")
for i in range(len(vlist)):
		if vlist[i] in list:
			rlist.append("yes")
			of.write("yes\n")
		else:
			rlist.append("no")
			of.write("no\n")
print(rlist)
of.close()
