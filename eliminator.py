import os
path = input('Enter CWD please :\n')
if len(path)<1:
	cwd = os.getcwd()
else:
	while path!="q":
		try:
			os.chdir(path)
		except:
			path=input("Invalid path\nIf you want to quit, then please write 'q'\nRemember to write windows' folder paths with the following format: C:\\xxx\\xxx\\xxx")
			continue
			
list=[]
fname=None
fname2=None
ofname=None

while fname!="q":
	try:
		fname=input("Please enter name of text file for keys with right values:\n")
		fhandle=open(fname)
	except:
		print("Invalid file name. Remember to put the '.txt' suffix at the end of the file\nYou can exit by typing 'q' in the terminal.")
		continue

for line in fhandle:
	word=line.strip()
	if word not in list:
		list.append(word)
fhandle.close()
			    
while fname2!="q":
	try:
		fname2=input("Please enter name of text file for list with values to be corrected:\n) 
		fhandle2=open(fname2)
	except:
		print("Invalid file name. Remember to put the '.txt' suffix at the end of the file\nYou can exit by typing 'q' in the terminal.")
		continue



vlist=[]
for line in fhandle2:
	word=line.strip()
	if word not in vlist:
		vlist.append(word)
rlist=[]

while ofname!="q":
	try:
		ofname=input("Please enter the name that you want for the output text file.\nRemember to put the '.txt' suffix at the end of the name.)
 		of=open(ofname,"w+")
	except:
		print("Invalid file name. Remember to put the '.txt' suffix at the end of the file\nYou can exit by typing 'q' in the terminal.")
		continue

for i in range(len(vlist)):
		if vlist[i] in list:
			rlist.append("yes")
			of.write("yes\n")
		else:
			rlist.append("no")
			of.write("no\n")
print(rlist)
of.close()
