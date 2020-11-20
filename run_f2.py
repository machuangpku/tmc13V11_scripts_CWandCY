import os


#需要修改的参数
homedir = os.getcwd()
dirpath = homedir + '\\'
cfgpath = dirpath + 'cfg\\octree-predlift\\'
datasetpath = 'E:\\mpeg-pcc-tmc13-master\\dataset\\'


tmc3 = 'tmc3_2.exe'
pce = 'pc_error_2.exe'
#os.mkdir('log')
logpath = 'log\\'

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
				'citytunnel_q1mm',
				'overpass_q1mm',
				'tollbooth_q1mm',
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

ford_01_file_lst = list()
ford_02_file_lst = list()
ford_03_file_lst = list()

num_lst1 = range(100,1000,1)
num_lst2 = range(1000,1600,1)
num_lst3 = range(200,1000,1)
num_lst4 = range(1000,1700,1)
num_lst5 = range(1,7,1)

for name4 in num_lst1:
		ford_01_file_lst.append( 'Ford_01_vox1mm-0' + str(name4))
for name5 in num_lst2:
		ford_01_file_lst.append( 'Ford_01_vox1mm-' + str(name5))
		
for name4 in num_lst1:
		ford_02_file_lst.append( 'Ford_02_vox1mm-0' + str(name4))
for name5 in num_lst2:
		ford_02_file_lst.append( 'Ford_02_vox1mm-' + str(name5))	
		
for name4 in num_lst3:
		ford_03_file_lst.append( 'Ford_03_vox1mm-0' + str(name4))
for name5 in num_lst4:
		ford_03_file_lst.append( 'Ford_03_vox1mm-' + str(name5))	
			
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
		
output = open('runLog_2.txt', 'w')
outputError = open('runDismatch_2.txt', 'w')

def getResolution(name2,num):
	pcerrorcfg = (cfgpath  + cond + '\\' + name2 + '\\' + num + '\\pcerror.cfg')
	reader = open( pcerrorcfg, 'r')
	Resolution = 0
	for line in reader:
		words = line.split()
		if ('resolution:' == words[0]):
			Resolution = int(words[1])
			break
	return str(Resolution)

def getPointCount(dec,declog,enclog):
	decfile = open(dec,'r')
	voxelnum = 0
	for line in decfile:
		words = line.split()
		if words[0]=='element' and words[1]=='vertex':
			voxelnum = words[2]
			break
	changedeclog  = open(enclog,'a')
	changedeclog.write('\nTotal point count: ' + voxelnum)
	changedeclog  = open(declog,'a')
	changedeclog.write('\nTotal point count: ' + voxelnum)

#运行start

#C1
cond = 'lossless-geom-lossy-attrs'
name1 = cond + '_'
C1_lst = ford_01_file_lst + ford_02_file_lst + ford_03_file_lst
for name2 in C1_lst:
	for num in C1_num_lst:
		name3 = ('_' + num)
		codname = (name1 + name2 + name3)
		cfgname2 = ('f' + name2[1:8] + 'q1mm')
		encconfig =(cfgpath  + cond + '\\' + cfgname2 + '\\' + num + '\\encoder.cfg')
		decconfig =(cfgpath  + cond + '\\' + cfgname2 + '\\' + num + '\\decoder.cfg')
		seq = (datasetpath + name2 + '.ply')
		enc = (name1 + name2 + name3 + '_enc.ply')
		dec = (name1 + name2 + name3 + '_dec.ply')
		bin = (name1 + name2 + name3 + '.bin')
		enclog = (logpath + name1 + name2 + name3  + '_enc.log')
		declog = (logpath + name1 + name2 + name3  + '_dec.log')
		pcelog = (logpath + name1 + name2 + name3  + '_pce.log')
		os.system(tmc3 + ' --config=' + encconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + enc + ' --compressedStreamPath=' + dirpath + bin + ' >' + enclog) 
		os.system(tmc3 + ' --config=' + decconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + dec + ' --compressedStreamPath=' + dirpath + bin + ' >' + declog) 
		os.system(pce + ' -a ' + seq + ' -b ' + dirpath + dec + ' -l 1 -d 1 -d 1 -r 30000 --nbThreads=10 --dropdups=2 --neighborsProc=1 >' + pcelog)
		getPointCount(dec,declog,enclog)		
		print(codname + ' finish')
		output.write(codname + ' finish\n')
		siez_enc = os.path.getsize(enc)
		siez_dec = os.path.getsize(dec)
		if siez_enc != siez_dec:
			outputError.write(codname+'\n')
		os.remove(enc)
		os.remove(dec)
		os.remove(bin)

		
#C2
cond = 'lossy-geom-lossy-attrs'
name1 = cond + '_'
C2_lst = list()
#ford_01_file_lst + ford_02_file_lst + ford_03_file_lst
for name2 in C2_lst:
	for num in C2_num_lst:
		name3 = ('_' + num) 
		codname = (name1 + name2 + name3)
		cfgname2 = ('f' + name2[1:8] + 'q1mm')
		encconfig =(cfgpath  + cond + '\\' + cfgname2 + '\\' + num + '\\encoder.cfg')
		decconfig =(cfgpath  + cond + '\\' + cfgname2 + '\\' + num + '\\decoder.cfg')
		seq = (datasetpath + name2 + '.ply')
		enc = (name1 + name2 + name3 + '_enc.ply')
		dec = (name1 + name2 + name3 + '_dec.ply')
		bin = (name1 + name2 + name3 + '.bin')
		enclog = (logpath + name1 + name2 + name3  + '_enc.log')
		declog = (logpath + name1 + name2 + name3  + '_dec.log')
		pcelog = (logpath + name1 + name2 + name3  + '_pce.log')
		os.system(tmc3 + ' --config=' + encconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + enc + ' --compressedStreamPath=' + dirpath + bin + ' >' + enclog) 
		os.system(tmc3 + ' --config=' + decconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + dec + ' --compressedStreamPath=' + dirpath + bin + ' >' + declog) 
		os.system(pce + ' -a ' + seq + ' -b ' + dirpath + dec + ' -n ' + seq + ' -l 1 -d 1 -d 1 -r 30000 --nbThreads=10 --dropdups=2 --neighborsProc=1 >' + pcelog)
		getPointCount(dec,declog,enclog)		
		print(codname + ' finish')
		output.write(codname + ' finish\n')
		siez_enc = os.path.getsize(enc)
		siez_dec = os.path.getsize(dec)
		if siez_enc != siez_dec:
			outputError.write(codname+'\n')
		os.remove(enc)
		os.remove(dec)
		os.remove(bin)

#CW		
cond = 'lossless-geom-lossless-attrs'
name1 = cond + '_'
CW_lst = list()
#ford_01_file_lst + ford_02_file_lst + ford_03_file_lst
for name2 in CW_lst:
	for num in CW_num_lst:
		name3 = ('_' + num) 
		codname = (name1 + name2 + name3)
		cfgname2 = ('f' + name2[1:8] + 'q1mm')
		encconfig =(cfgpath  + cond + '\\' + cfgname2 + '\\encoder.cfg')
		decconfig =(cfgpath  + cond + '\\' + cfgname2 + '\\decoder.cfg')
		seq = (datasetpath + name2 + '.ply')
		enc = (name1 + name2 + name3 + '_enc.ply')
		dec = (name1 + name2 + name3 + '_dec.ply')
		bin = (name1 + name2 + name3 + '.bin')
		enclog = (logpath + name1 + name2 + name3  + '_enc.log')
		declog = (logpath + name1 + name2 + name3  + '_dec.log')
		os.system(tmc3 + ' --config=' + encconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + enc + ' --compressedStreamPath=' + dirpath + bin + ' >' + enclog) 
		os.system(tmc3 + ' --config=' + decconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + dec + ' --compressedStreamPath=' + dirpath + bin + ' >' + declog) 
		getPointCount(dec,declog,enclog)
		print(codname + ' finish')
		output.write(codname + ' finish\n')
		siez_enc = os.path.getsize(enc)
		siez_dec = os.path.getsize(dec)
		if siez_enc != siez_dec:
			outputError.write(codname+'\n')
		os.remove(enc)
		os.remove(dec)
		os.remove(bin)

#CY		
cond = 'lossless-geom-nearlossless-attrs'
name1 = cond + '_'
CY_lst = list()
#ford_01_file_lst + ford_02_file_lst + ford_03_file_lst
for name2 in CY_lst:
	for num in CY_num_lst:
		name3 = ('_' + num) 
		codname = (name1 + name2 + name3)
		cfgname2 = ('f' + name2[1:8] + 'q1mm')
		encconfig =(cfgpath  + cond + '\\' + cfgname2 + '\\' + num + '\\encoder.cfg')
		decconfig =(cfgpath  + cond + '\\' + cfgname2 + '\\' + num + '\\decoder.cfg')
		seq = (datasetpath + name2 + '.ply')
		enc = (name1 + name2 + name3 + '_enc.ply')
		dec = (name1 + name2 + name3 + '_dec.ply')
		bin = (name1 + name2 + name3 + '.bin')
		enclog = (logpath + name1 + name2 + name3  + '_enc.log')
		declog = (logpath + name1 + name2 + name3  + '_dec.log')
		pcelog = (logpath + name1 + name2 + name3  + '_pce.log')
		os.system(tmc3 + ' --config=' + encconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + enc + ' --compressedStreamPath=' + dirpath + bin + ' >' + enclog) 
		os.system(tmc3 + ' --config=' + decconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + dec + ' --compressedStreamPath=' + dirpath + bin + ' >' + declog) 
		os.system(pce + ' -a ' + seq + ' -b ' + dirpath + dec + ' -l 1 -d 1 -d 1 -r 30000 --nbThreads=10 --dropdups=2 --neighborsProc=1 >' + pcelog)
		getPointCount(dec,declog,enclog)
		print(codname + ' finish')
		output.write(codname + ' finish\n')
		siez_enc = os.path.getsize(enc)
		siez_dec = os.path.getsize(dec)
		if siez_enc != siez_dec:
			outputError.write(codname+'\n')
		os.remove(enc)
		os.remove(dec)
		os.remove(bin)

#运行end
outputError.close()


			

		
