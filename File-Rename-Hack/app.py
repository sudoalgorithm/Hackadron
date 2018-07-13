import os
path = '<Path Of Your Dir>'
c = 0
for filename in os.listdir(path):
	fileN = os.path.join(path,filename)
	fileToRename = os.path.join(path, <Filename you want>)
	os.rename(fileN, fileToRename)
	c += 1
