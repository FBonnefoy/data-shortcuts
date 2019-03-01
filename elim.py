import os
cwd = os.getcwd()
cwd
fname="keys.txt"
fhandle=open(fname)
list=[]
for line in fhandle:
	word=line.strip()
	word=str(word)
	if word not in list:
		list.append(word)

fhandle.close()
fname2="listtocorrect.txt"
fhandle2=open(fname2)
vlist=[]
for line in fhandle2:
	word=line.strip()
	word=str(word)
	if word not in vlist:
		vlist.append(word)

rlist=[]
ofname="out.txt"
of=open(ofname,"w+")
for i in range(len(vlist)):
		if vlist[i] in list:
			rlist.append("yes")
			of.write("yes\n")
		else:
			rlist.append("no")
			of.write("no\n")

of.close()
