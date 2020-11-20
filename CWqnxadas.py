from win32com.client import Dispatch
import win32com.client
import os

# 获取excel 对象
homedir = os.getcwd()
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

qnxadas_junction_approach = list()
qnxadas_junction_exit = list()
qnxadas_motorway_join = list()
qnxadas_navigating_bends = list()

frame_list = list([
'qnxadas-junction-approach',
'qnxadas-junction-exit',
'qnxadas-motorway-join',
'qnxadas-navigating-bends',
])

num_lst1 = range(1,75,1)
num_lst2 = range(1,75,1)
num_lst3 = range(1,501,1)
num_lst4 = range(1,301,1)
num_lst5 = range(0,4,1)

for name4 in num_lst1:
		qnxadas_junction_approach.append(str(name4).zfill(6))
		
for name4 in num_lst2:
		qnxadas_junction_exit.append(str(name4).zfill(6))
		
for name4 in num_lst3:
		qnxadas_motorway_join.append(str(name4).zfill(6))
	
for name4 in num_lst4:
		qnxadas_navigating_bends.append(str(name4).zfill(6))
	
			
C1_num_lst = list([
				'r01',
				'r02',
				'r03',
				'r04',
				'r05',
				'r06',
        ])
		
C2_num_lst = list([
				'r01',
				'r02',
				'r03',
				'r04',
				'r05',
				'r06',
        ])
		
CW_num_lst = list([
				'r01',
        ])
		
CY_num_lst = list([
				'r01',
				'r02',
				'r03',
				'r04',
				'r05',
        ])

cond = 'lossless-geom-lossless-attrs'
name1 = cond + '_'
C1_lst =  list([
qnxadas_junction_approach,
qnxadas_junction_exit,
qnxadas_motorway_join,
qnxadas_navigating_bends,
])

pc=57

for frame_num in num_lst5:

	for num in CW_num_lst:
		points = 0
		total = 0
		positions = 0
		reflectances = 0
		time = 0
		time2 = 0
		for name2 in C1_lst[frame_num]:
			
			frame_name = frame_list[frame_num]
			name3 = ('_' + num)
			codname = (name1 + frame_name + name2 + name3)

			enclog = (logpath + codname  + '_enc.log')
			declog = (logpath + codname  + '_dec.log')
		
			reader = open( enclog, 'r')

			tmppos = 0
			tmpref = 0
			for line in reader:
				words = line.split()
				if (('Total' in words) and ('point' in words)) :
					points+= int(words[3])
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
			

			reader = open(declog)
			for line in reader:
				words = line.split()
				if ('(user):' in words)and(words[0]=='Processing'):
					time2+=float(words[3])
			reader.close()
			
		mySheet.Cells(pc, 36).Value = time2
		mySheet.Cells(pc, 30).Value = points
		mySheet.Cells(pc, 31).Value = total
		mySheet.Cells(pc, 32).Value = positions
		mySheet.Cells(pc, 34).Value = reflectances
		mySheet.Cells(pc, 35).Value = time
		pc=pc+1

# 保存
myBook.save

# 退出
myBook.close


