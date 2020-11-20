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
mySheet = myBook.Worksheets("CY losslG,nearllA,intra")

condition_lst = list([
					'lossless-geom-nearlossless-attrs_',
        ])
		
catA_lst = list([
				'basketball_player_vox11_00000200',
				'boxer_viewdep_vox12',
				'dancer_vox11_00000001',
				'egyptian_mask_vox12',
				'facade_00009_vox12',
				'facade_00015_vox14',
				'facade_00064_vox11',
				'frog_00067_vox12',
				'head_00039_vox12',
				'house_without_roof_00057_vox12',
				'longdress_viewdep_vox12',
				'longdress_vox10_1300',
				'loot_viewdep_vox12',
				'loot_vox10_1200',
				'queen_0200',
				'redandblack_viewdep_vox12',
				'redandblack_vox10_1550',
				'shiva_00035_vox12',
				'soldier_viewdep_vox12',
				'soldier_vox10_0690',
				'thaidancer_viewdep_vox12',
				'ulb_unicorn_vox13',
])

catB_lst = list([				
				'arco_valentino_dense_vox12',
				'arco_valentino_dense_vox20',
				'egyptian_mask_vox20',
				'facade_00009_vox20',
				'facade_00015_vox20',
				'facade_00064_vox14',
				'facade_00064_vox20',
				'frog_00067_vox20',
				'head_00039_vox20',
				'house_without_roof_00057_vox20',
				'landscape_00014_vox14',
				'landscape_00014_vox20',
				'palazzo_carignano_dense_vox14',
				'palazzo_carignano_dense_vox20',
				'shiva_00035_vox20',
				'stanford_area_2_vox16',
				'stanford_area_2_vox20',
				'stanford_area_4_vox16',
				'stanford_area_4_vox20',
				'staue_klimt_vox12',
				'staue_klimt_vox20',
				'ulb_unicorn_hires_vox15',
				'ulb_unicorn_hires_vox20',
				'ulb_unicorn_vox20',
])	
cat3_fused_list= list([				
				'citytunnel_q1mm',
				'overpass_q1mm',
				'tollbooth_q1mm',
])	
name_lst = catA_lst +catB_lst+ cat3_fused_list

num_lst = list([
				'_r01',
				'_r02',
				'_r03',
				'_r04',
				'_r05',
        ])
output = open('enc_result.txt', 'w')

file_lst = list()
for name1 in condition_lst:
	for name2 in name_lst:
		for name3 in num_lst:
			file_lst.append( name1 + name2 + name3)

pc=5

for file_name in file_lst:

	record = list()

	points = 0
	total = 0
	geom = 0
	color = 0
	reflect = 0
	timeE = 0
	timeD = 0
	Y = 0 
	U = 0
	V = 0
	R = 0
	Yh = 0 
	Uh = 0
	Vh = 0
	Rh = 0

	readerE = open( logpath + file_name+'_enc.log', 'r')
	for line in readerE:
		words = line.split()
		if (('Total' in words) and ('bitstream' in words)) :
			total = int(words[3])*8
		if (('positions' in words) and ('bitstream' in words)) :
			geom += int(words[3])*8
		if (('colors' in words) and ('bitstream' in words)) :
			color += int(words[3])*8
		if (('reflectances' in words) and ('bitstream' in words)) :
			reflect += int(words[3])*8
		if ('(user):' in words)and(words[0]=='Processing'):
			timeE = words[3]

	readerD = open( logpath + file_name+'_dec.log', 'r')
	for line in readerD:
		words = line.split()
		if (('Total' in words) and ('point' in words)) :
			points = int(words[3])
		if ('(user):' in words)and(words[0]=='Processing'):
			timeD = words[3]


	readerD = open( logpath + file_name+'_pce.log', 'r')
	for line in readerD:
		words = line.split()
		if ('c[0],PSNRF' in words):
			Y=float(words[2])
		if ('c[1],PSNRF' in words):
			U=float(words[2])
		if ('c[2],PSNRF' in words):
			V=float(words[2])
		if ('r,PSNR' in words) and ('F' in words):
			R=float(words[3])
		if ('h.c[0],PSNRF' in words):
			Yh=float(words[2])
		if ('h.c[1],PSNRF' in words):
			Uh=float(words[2])
		if ('h.c[2],PSNRF' in words):
			Vh=float(words[2])
		if ('h.r,PSNR' in words) and ('F' in words):
			Rh=float(words[3])

	record.append(str(points))
	mySheet.Cells(pc, 37).Value = points
	
	
	
	record.append(str(total))
	mySheet.Cells(pc, 38).Value = total
	record.append(str(geom))
	mySheet.Cells(pc, 39).Value = geom
	if color != 0:
		record.append(str(color)) 
		mySheet.Cells(pc, 40).Value = color
	if reflect != 0:
		record.append(str(reflect)) 
		mySheet.Cells(pc, 41).Value = reflect
	if Y != 0:
		record.append(str(Y)) 
		mySheet.Cells(pc, 42).Value = Y
	if U != 0:
		record.append(str(U)) 
		mySheet.Cells(pc, 43).Value = U
	if V != 0:
		record.append(str(V)) 
		mySheet.Cells(pc, 44).Value = V
	if R != 0:
		record.append(str(R)) 
		mySheet.Cells(pc, 45).Value = R
	if Yh != 0:
		record.append(str(Yh)) 
		mySheet.Cells(pc, 46).Value = Yh
	if Uh != 0:
		record.append(str(Uh)) 
		mySheet.Cells(pc, 47).Value = Uh
	if Vh != 0:
		record.append(str(Vh)) 
		mySheet.Cells(pc, 48).Value = Vh
	if Rh != 0:
		record.append(str(Rh)) 
		mySheet.Cells(pc, 49).Value = Rh
		
	record.append(str(timeE)) 
	mySheet.Cells(pc, 50).Value = timeE
	record.append(str(timeD)) 
	mySheet.Cells(pc, 51).Value = timeD
	readerE.close()
	readerD.close()
	record_str = ''
	pc=pc+1

	for word in record:
		record_str = record_str + str(word) + ' '
	record_str = record_str + '\n'
	output.write(record_str)

output.close()

# 保存
myBook.save

# 退出
myBook.close