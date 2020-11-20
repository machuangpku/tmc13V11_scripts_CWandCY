import os


#需要修改的参数
homedir = os.getcwd()
dirpath = homedir + '\\'
cfgpath = dirpath + 'cfg\\octree-predlift\\'
datasetpath = 'E:\\mpeg-pcc-tmc13-master\\dataset\\'


tmc3 = 'tmc3_6.exe'
pce = 'pc_error_6.exe'
#os.mkdir('log')
logpath = 'log\\'


ford_01_file_lst = list()
ford_02_file_lst = list()
ford_03_file_lst = list()

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
		
output = open('runLog_4.txt', 'w')
outputError = open('runDismatch_4.txt', 'w')

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
C1_lst =  list([
qnxadas_junction_approach,
qnxadas_junction_exit,
qnxadas_motorway_join,
qnxadas_navigating_bends,
])

for frame_num in num_lst5:
	for name2 in C1_lst[frame_num]:
		for num in C1_num_lst:
			frame_name = frame_list[frame_num]
			name3 = ('_' + num)
			codname = (name1 + frame_name + name2 + name3)
			encconfig =(cfgpath  + cond + '\\' + frame_name + '\\' + num + '\\encoder.cfg')
			decconfig =(cfgpath  + cond + '\\' + frame_name + '\\' + num + '\\decoder.cfg')
			seq = (datasetpath + frame_name + '\\' + frame_name + '\\' + name2 + '.ply')
			enc = (codname + '_enc.ply')
			dec = (codname + '_dec.ply')
			bin = (codname + '.bin')
			enclog = (logpath + codname  + '_enc.log')
			declog = (logpath + codname  + '_dec.log')
			pcelog = (logpath + codname  + '_pce.log')
			os.system(tmc3 + ' --config=' + encconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + enc + ' --compressedStreamPath=' + dirpath + bin + ' >' + enclog) 
			os.system(tmc3 + ' --config=' + decconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + dec + ' --compressedStreamPath=' + dirpath + bin + ' >' + declog) 
			os.system(pce + ' -a ' + seq + ' -b ' + dirpath + dec + ' -c 1 -l 1 -d 1 -r 30000 --nbThreads=10 --dropdups=2 --neighborsProc=1 >' + pcelog) 
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
C2_lst =  list([
qnxadas_junction_approach,
qnxadas_junction_exit,
qnxadas_motorway_join,
qnxadas_navigating_bends,
])
for frame_num in num_lst5:
	for name2 in C2_lst[frame_num]:
		for num in C2_num_lst:
			frame_name = frame_list[frame_num]
			name3 = ('_' + num)
			codname = (name1 + frame_name + name2 + name3)
			encconfig =(cfgpath  + cond + '\\' + frame_name + '\\' + num + '\\encoder.cfg')
			decconfig =(cfgpath  + cond + '\\' + frame_name + '\\' + num + '\\decoder.cfg')
			seq = (datasetpath + frame_name + '\\' + frame_name + '\\' + name2 + '.ply')
			seqnormal = (datasetpath + frame_name + '\\' + frame_name + '\\' + name2 + '_n.ply')
			enc = (codname + '_enc.ply')
			dec = (codname + '_dec.ply')
			bin = (codname + '.bin')
			enclog = (logpath + codname  + '_enc.log')
			declog = (logpath + codname  + '_dec.log')
			pcelog = (logpath + codname  + '_pce.log')
			os.system(tmc3 + ' --config=' + encconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + enc + ' --compressedStreamPath=' + dirpath + bin + ' >' + enclog) 
			os.system(tmc3 + ' --config=' + decconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + dec + ' --compressedStreamPath=' + dirpath + bin + ' >' + declog) 
			os.system(pce + ' -a ' + seq + ' -b ' + dirpath + dec + ' -n ' + seqnormal + ' -c 1 -l 1 -d 1 -r 30000 --nbThreads=10 --dropdups=2 --neighborsProc=1 ' + ' >' + pcelog) 
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
CW_lst = list([
qnxadas_junction_approach,
qnxadas_junction_exit,
qnxadas_motorway_join,
qnxadas_navigating_bends,
])
for frame_num in num_lst5:
	for name2 in CW_lst[frame_num]:
		for num in CW_num_lst:
			frame_name = frame_list[frame_num]
			name3 = ('_' + num)
			codname = (name1 + frame_name + name2 + name3)
			encconfig =(cfgpath  + cond + '\\' + frame_name + '\\encoder.cfg')
			decconfig =(cfgpath  + cond + '\\' + frame_name + '\\decoder.cfg')
			seq = (datasetpath + frame_name + '\\' + frame_name + '\\' + name2 + '.ply')
			enc = (codname + '_enc.ply')
			dec = (codname + '_dec.ply')
			bin = (codname + '.bin')
			enclog = (logpath + codname  + '_enc.log')
			declog = (logpath + codname  + '_dec.log')
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
CY_lst = list([
qnxadas_junction_approach,
qnxadas_junction_exit,
qnxadas_motorway_join,
qnxadas_navigating_bends,
])
for frame_num in num_lst5:
	for name2 in CY_lst[frame_num]:
		for num in CY_num_lst:
			frame_name = frame_list[frame_num]
			name3 = ('_' + num)
			codname = (name1 + frame_name + name2 + name3)
			encconfig =(cfgpath  + cond + '\\' + frame_name + '\\' + num + '\\encoder.cfg')
			decconfig =(cfgpath  + cond + '\\' + frame_name + '\\' + num + '\\decoder.cfg')
			seq = (datasetpath + frame_name + '\\' + frame_name + '\\' + name2 + '.ply')
			enc = (codname + '_enc.ply')
			dec = (codname + '_dec.ply')
			bin = (codname + '.bin')
			enclog = (logpath + codname  + '_enc.log')
			declog = (logpath + codname  + '_dec.log')
			pcelog = (logpath + codname  + '_pce.log')
			os.system(tmc3 + ' --config=' + encconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + enc + ' --compressedStreamPath=' + dirpath + bin + ' >' + enclog) 
			os.system(tmc3 + ' --config=' + decconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + dec + ' --compressedStreamPath=' + dirpath + bin + ' >' + declog) 
			os.system(pce + ' -a ' + seq + ' -b ' + dirpath + dec + ' -c 1 -l 1 -d 1 -r 30000 --nbThreads=10 --dropdups=2 --neighborsProc=1 >' + pcelog) 
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

			

		
