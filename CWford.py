from win32com.client import Dispatch
import win32com.client
import os

logpath = 'log\\'
homedir = os.getcwd()
# 获取excel 对象

excel = win32com.client.Dispatch('Excel.Application')
"""
0代表隐藏对象，但可以通过菜单再显示
-1代表显示对象
2代表隐藏对象，但不可以通过菜单显示，只能通过VBA修改为显示状态
"""
excel.Visible = -1

# 打开excel
myBook = excel.Workbooks.Open(homedir + "\\tmc13anchor.xlsm")

# sheet页，可以是序号，也可以是名称
mySheet = myBook.Worksheets("CW losslG,losslA,intra")

logpath = 'log\\'
condition = (logpath + 'lossless-geom-lossless-attrs')
num_lst1 = range(100,1000,1)
num_lst2 = range(1000,1600,1)
num_lst3 = range(200,1000,1)
num_lst4 = range(1000,1700,1)
num_lst5 = list([
				'_r01',
        ])

pc=54
output1 = open('ford1_B.txt', 'w')
for name6 in num_lst5:
	file_lst = list()
	for name4 in num_lst1:
			file_lst.append( condition + '_Ford_01_vox1mm-0' + str(name4) + str(name6) + '_enc.log')


	for name5 in num_lst2:
			file_lst.append( condition + '_Ford_01_vox1mm-' + str(name5) + str(name6) + '_enc.log')

	points = 0
	total = 0
	positions = 0
	reflectances = 0
	time = 0

	for file_name in file_lst:
		record = list()
		reader = open( file_name, 'r')
		tmppos = 0
		tmpref = 0
		for line in reader:
			words = line.split()
			if (('Total' in words) and ('point' in words)) :
				points+=int(words[3])
			if (('positions' in words) and ('bitstream' in words)):
				tmppos=int(words[3])*8
			if (('reflectances' in words) and ('bitstream' in words)):
				tmpref=int(words[3])*8
			if (('Total' in words) and ('bitstream' in words)):
				total+=int(words[3])*8
				positions+=tmppos
				reflectances+=tmpref
			if ('(user):' in words)and(words[0]=='Processing'):
				time+=float(words[3])
		reader.close()

	if points != 0:
		record.append(str(points)) 
		mySheet.Cells(pc, 30).Value = points
	record.append(str(total)) 
	mySheet.Cells(pc, 31).Value = total
	record.append(str(positions)) 
	mySheet.Cells(pc, 32).Value = positions
	record.append(str(reflectances)) 
	mySheet.Cells(pc, 34).Value = reflectances
	record.append(str(time)) 
	mySheet.Cells(pc, 35).Value = time

	record_str = ''
	for word in record:
		record_str = record_str + str(word) + ' '
	record_str = record_str + '\n'
	output1.write(record_str)
output1.close()

pc=55
output2 = open('ford2_B.txt', 'w')
for name6 in num_lst5:
	file_lst = list()
	for name4 in num_lst1:
			file_lst.append( condition + '_Ford_02_vox1mm-0' + str(name4) + str(name6) + '_enc.log')


	for name5 in num_lst2:
			file_lst.append( condition + '_Ford_02_vox1mm-' + str(name5) + str(name6) + '_enc.log')

	points = 0
	total = 0
	positions = 0
	reflectances = 0
	time = 0

	for file_name in file_lst:
		record = list()
		reader = open( file_name, 'r')
		tmppos = 0
		tmpref = 0
		for line in reader:
			words = line.split()
			if (('Total' in words) and ('point' in words)) :
				points+=int(words[3])
			if (('positions' in words) and ('bitstream' in words)):
				tmppos=int(words[3])*8
			if (('reflectances' in words) and ('bitstream' in words)):
				tmpref=int(words[3])*8
			if (('Total' in words) and ('bitstream' in words)):
				total+=int(words[3])*8
				positions+=tmppos
				reflectances+=tmpref
			if ('(user):' in words)and(words[0]=='Processing'):
				time+=float(words[3])
		reader.close()

	if points != 0:
		record.append(str(points)) 
		mySheet.Cells(pc, 30).Value = points
	record.append(str(total)) 
	mySheet.Cells(pc, 31).Value = total
	record.append(str(positions)) 
	mySheet.Cells(pc, 32).Value = positions
	record.append(str(reflectances)) 
	mySheet.Cells(pc, 34).Value = reflectances
	record.append(str(time)) 
	mySheet.Cells(pc, 35).Value = time

	record_str = ''
	for word in record:
		record_str = record_str + str(word) + ' '
	record_str = record_str + '\n'
	output2.write(record_str)
output2.close()

pc=56
output3 = open('ford3_B.txt', 'w')
for name6 in num_lst5:
	file_lst = list()
	for name4 in num_lst3:
			file_lst.append( condition + '_Ford_03_vox1mm-0' + str(name4) + str(name6) + '_enc.log')


	for name5 in num_lst4:
			file_lst.append( condition + '_Ford_03_vox1mm-' + str(name5) + str(name6) + '_enc.log')

	points = 0
	total = 0
	positions = 0
	reflectances = 0
	time = 0

	for file_name in file_lst:
		record = list()
		reader = open( file_name, 'r')
		tmppos = 0
		tmpref = 0
		for line in reader:
			words = line.split()
			if (('Total' in words) and ('point' in words)) :
				points+=int(words[3])
			if (('positions' in words) and ('bitstream' in words)):
				tmppos=int(words[3])*8
			if (('reflectances' in words) and ('bitstream' in words)):
				tmpref=int(words[3])*8
			if (('Total' in words) and ('bitstream' in words)):
				total+=int(words[3])*8
				positions+=tmppos
				reflectances+=tmpref
			if ('(user):' in words)and(words[0]=='Processing'):
				time+=float(words[3])
		reader.close()

	if points != 0:
		record.append(str(points)) 
		mySheet.Cells(pc, 30).Value = points
	record.append(str(total)) 
	mySheet.Cells(pc, 31).Value = total
	record.append(str(positions)) 
	mySheet.Cells(pc, 32).Value = positions
	record.append(str(reflectances)) 
	mySheet.Cells(pc, 34).Value = reflectances
	record.append(str(time)) 
	mySheet.Cells(pc, 35).Value = time

	record_str = ''
	for word in record:
		record_str = record_str + str(word) + ' '
	record_str = record_str + '\n'
	output3.write(record_str)
output3.close()

pc=54
output4 = open('ford1_D.txt', 'w')
for name6 in num_lst5:
	file_lst = list()
	for name4 in num_lst1:
			file_lst.append( condition + '_Ford_01_vox1mm-0' + str(name4) + str(name6) + '_dec.log')


	for name5 in num_lst2:
			file_lst.append( condition + '_Ford_01_vox1mm-' + str(name5) + str(name6) + '_dec.log')

	time2 = 0

	for file_name in file_lst:
		record = list()
		reader = open( file_name, 'r')
		for line in reader:
			words = line.split()
			if ('(user):' in words)and(words[0]=='Processing'):
				time2+=float(words[3])

	reader.close()
	
	record.append(str(time2)) 
	mySheet.Cells(pc, 36).Value = time2

	record_str = ''
	for word in record:
		record_str = record_str + str(word) + ' '
	record_str = record_str + '\n'
	output4.write(record_str)
output4.close()

pc=55
output5 = open('ford2_D.txt', 'w')
for name6 in num_lst5:
	file_lst = list()
	for name4 in num_lst1:
			file_lst.append( condition + '_Ford_02_vox1mm-0' + str(name4) + str(name6) + '_dec.log')


	for name5 in num_lst2:
			file_lst.append( condition + '_Ford_02_vox1mm-' + str(name5) + str(name6) + '_dec.log')

	time2 = 0

	for file_name in file_lst:
		record = list()
		reader = open( file_name, 'r')
		for line in reader:
			words = line.split()
			if ('(user):' in words)and(words[0]=='Processing'):
				time2+=float(words[3])
	reader.close()
	
	record.append(str(time2)) 
	mySheet.Cells(pc, 36).Value = time2

	record_str = ''
	for word in record:
		record_str = record_str + str(word) + ' '
	record_str = record_str + '\n'
	output5.write(record_str)
output5.close()

pc=56
output6 = open('ford3_D.txt', 'w')
for name6 in num_lst5:
	file_lst = list()
	for name4 in num_lst3:
			file_lst.append( condition + '_Ford_03_vox1mm-0' + str(name4) + str(name6) + '_dec.log')


	for name5 in num_lst4:
			file_lst.append( condition + '_Ford_03_vox1mm-' + str(name5) + str(name6) + '_dec.log')

	time2 = 0

	for file_name in file_lst:
		record = list()
		reader = open( file_name, 'r')
		for line in reader:
			words = line.split()
			if ('(user):' in words)and(words[0]=='Processing'):
				time2+=float(words[3])

	reader.close()

	record.append(str(time2)) 
	mySheet.Cells(pc, 36).Value = time2

	record_str = ''
	for word in record:
		record_str = record_str + str(word) + ' '
	record_str = record_str + '\n'
	output6.write(record_str)
output6.close()


# 保存
myBook.save

# 退出
myBook.close