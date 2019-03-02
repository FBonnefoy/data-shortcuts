import os
import sys
path = input('Enter CWD please :\n')
if len(path)<1:
	cwd = os.getcwd()
else:
	while True:
		try:
			os.chdir(path)
			break
		except:
			if len(path)<1:
				cwd = os.getcwd()
				break
			if path=='quit':
				break
			path=input("\n\nInvalid path\n\nIf you want to quit, then please write 'quit'\n\nRemember to write windows' folder paths with the following format: C:\\xxx\\xxx\\xxx\n\nPress Enter if you want to select the current working directory\n\n\n")
			continue

if path=='quit':
	sys.exit()
print("\n")
list=[]
fname=None
fname2=None
ofname=None

while True:
	try:
		fname=input("\nPlease enter name of text file for keys with right values:\n")
		if fname=='quit':
					break
		fhandle=open(fname)
		break
	except:
		print("\nInvalid file name. Remember to put the '.txt' suffix at the end of the file\nYou can exit by typing 'quit' in the terminal.")
		print("\n")
		continue
	finally:
		if path=='quit':
			break

if fname=='quit':
	sys.exit()

for line in fhandle:
	word=line.strip()
	if word not in list:
		list.append(word)
fhandle.close()

while True:
	try:
		fname2=input("\nPlease enter name of text file for list with values to be corrected:\n")
		if fname2=='quit':
			break
		fhandle2=open(fname2)
		break
	except:
		print("\nInvalid file name. Remember to put the '.txt' suffix at the end of the file\nYou can exit by typing 'quit' in the terminal.\n")
		continue


if fname2=='quit':
	sys.exit()

vlist=[]
for line in fhandle2:
	word=line.strip()
	if word not in vlist:
		vlist.append(word)
rlist=[]

ofname=input("\nPlease enter the name that you want for the output text file.\nRemember to put the '.txt' suffix at the end of the name.\n")
while True:
	try:
		if ofname=='quit':
					break
		if ofname.endswith(".txt"):
			of=open(ofname,"w")
			break
		else:
			print("\nInvalid file name. Remember to put the '.txt' suffix at the end of the file\nYou can exit by typing 'quit' in the terminal.\n")
			ofname=input("\n\nPlease enter file name again\n")
			continue

	except:
		print("\nInvalid file name. Remember to put the '.txt' suffix at the end of the file\nYou can exit by typing 'quit' in the terminal.\n")
		ofname=input("\n\nPlease enter file name again\n\n")
		continue


if ofname=='quit':
	sys.exit()

for i in range(len(vlist)):
	if vlist[i] in list:
		rlist.append("yes")
		of.write("yes\n")
	else:
		rlist.append("no")
		of.write("no\n")
print("\n\nBye!")
of.close()
