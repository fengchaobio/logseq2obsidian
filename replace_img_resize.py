import os
import re

def replace(file,path):
	# print(file)
	file = path+file
	with open(file,'r') as f:
		content = []
		for i in f.readlines():
			# print(i)
			i = re.sub('{:.*}','',i)
			content.append(i)
			print(i)

	with open(file,'w') as f:
		for i in content:
			f.write(i)

def main(dir):
	files = os.listdir(dir)
	files.remove('.DS_Store')
	print(f"共计{len(files)}个文件")
	for file in files:
		replace(file,path)


path = '/Users/fengchao/Desktop/note/journals/'

main(path)