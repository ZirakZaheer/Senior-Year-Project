import os
import subprocess
import sys


proc=subprocess.Popen('python vol.py -f /home/xen/Documents/zeus.vmem pslist', shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]

count = 0
index = 0
arrayOfFiles=['Offset.txt','Name.txt','PID.txt','PPID.txt','Thds.txt','Hnds.txt','Sess.txt','Wow64.txt','Start.txt','Start.txt','Start.txt','Exit.txt','Exit.txt','Exit.txt','temp.txt']
for x in arrayOfFiles:
	if os.path.exists(x):
		os.remove(x)
for oneLine in output.split("\n"):
	if count < 2:
		count = count+1
		continue
	index = 0
	for oneWord in oneLine.split():
		commandToExecute= "python AppendToFileNewLine.py " + arrayOfFiles[index] + " " + oneWord
		index = index+1
		os.system(commandToExecute)

