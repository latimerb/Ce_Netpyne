from netpyne import specs, sim
from random import randint
from numpy import *

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters
netParams.sizeX = 100 #horizontal axis in um
netParams.sizeY = 100 #horizontal axis in um
netParams.sizeZ = 1000 #vertical axis in um


# Load Inputs from files
# We load the inputs, put them into a list and create them in the popParams section
cellsList=[]

LAf=[]
LAfList = []
for i in range(1,21):
	file = open('Data_Input/Input_laf{}.dat'.format(i)) #Import our input files 
	LAf.append(file.read().splitlines())
	LAf[i-1]=map(float,LAf[i-1]) #This is needed to convert from strings to numbers
	LAfList.append({'cellLabel':'laf{}'.format(i),'x':randint(0,45),'y':randint(0,50),'z':randint(0,50),'spkTimes':LAf[i-1]})
	
LAer=[]
LAerList=[]
for i in range(1,21):
	file = open('Data_Input/Input_laer{}.dat'.format(i)) #Import our input files 
	LAer.append(file.read().splitlines())
	LAer[i-1]=map(float,LAer[i-1]) #This is needed to convert from strings to numbers
	LAerList.append({'cellLabel':'laer{}'.format(i), 'x':randint(0,45),'y':randint(0,50),'z':randint(0,50),'spkTimes':LAer[i-1]})

BAf=[]
BAfList=[]
for i in range(1,21):
	file = open('Data_Input/Input_baf{}.dat'.format(i)) #Import our input files 
	BAf.append(file.read().splitlines())
	BAf[i-1]=map(float,BAf[i-1]) #This is needed to convert from strings to numbers
	BAfList.append({'cellLabel':'baf{}'.format(i),'x':randint(0,45),'y':randint(50,100),'z':randint(0,50), 'spkTimes':BAf[i-1]})

BAer=[]
BAerList=[]
for i in range(1,21):
	file = open('Data_Input/Input_baer{}.dat'.format(i)) #Import our input files 
	BAer.append(file.read().splitlines())
	BAer[i-1]=map(float,BAer[i-1]) #This is needed to convert from strings to numbers
	BAerList.append({'cellLabel':'baer{}'.format(i), 'x':randint(0,45),'y':randint(50,100),'z':randint(0,50),'spkTimes':BAer[i-1]})
	
ITCd=[]
ITCdList=[]
for i in range(1,21):
	file = open('Data_Input/Input_itcd{}.dat'.format(i)) #Import our input files 
	ITCd.append(file.read().splitlines())
	ITCd[i-1]=map(float,ITCd[i-1]) #This is needed to convert from strings to numbers
	ITCdList.append({'cellLabel':'itcd{}'.format(i), 'x':randint(45,55),'y':randint(25,40),'z':randint(0,50),'spkTimes':ITCd[i-1]})

ITCv=[]
ITCvList=[]
for i in range(1,21):
	file = open('Data_Input/Input_itcv{}.dat'.format(i)) #Import our input files 
	ITCv.append(file.read().splitlines())
	ITCv[i-1]=map(float,ITCv[i-1]) #This is needed to convert from strings to numbers
	ITCvList.append({'cellLabel':'itcv{}'.format(i),'x':randint(45,55),'y':randint(65,80),'z':randint(0,50), 'spkTimes':ITCv[i-1]})

## Cell property rules
# This is where we import the cell type classes from the template.py file. cellName must match exactly with the name in the template.py file.
netParams.importCellParams(label='RegularSpiking', conds= {'cellType': 'RS', 'cellModel': 'CE_Template'}, 
	fileName='CE_template.py', cellName='RegularSpiking')

netParams.importCellParams(label='Low-Threshold Bursting', conds= {'cellType': 'LTB', 'cellModel': 'CE_Template'}, 
	fileName='CE_template.py', cellName='LowThresholdBursting')
	
netParams.importCellParams(label='Late Firing', conds= {'cellType': 'LF', 'cellModel': 'CE_Template'}, 
	fileName='CE_template.py', cellName='LateFiring')
	
	

## Population parameters
# This is where we define how many cells there are of each type
# The name in the brackets is an arbitrary label we give to that particular population. 

netParams.popParams['LAf'] = {'cellModel' : 'VecStim', 'numCells': 20, 'cellsList': LAfList}
netParams.popParams['LAer'] = {'cellModel' : 'VecStim', 'numCells': 20, 'cellsList': LAerList}
netParams.popParams['BAf'] = {'cellModel' : 'VecStim', 'numCells': 20, 'cellsList': BAfList}
netParams.popParams['BAer'] = {'cellModel' : 'VecStim', 'numCells': 20, 'cellsList': BAerList}
#netParams.popParams['ITCd'] = {'cellModel' : 'VecStim', 'numCells': 20, 'cellsList': ITCdList}
#netParams.popParams['ITCv'] = {'cellModel' : 'VecStim', 'numCells': 20, 'cellsList': ITCvList}

netParams.popParams['PKCdM_RS'] = {'cellType': 'RS', 'numCells': 5, 'xRange':[55,100],'yRange':[0,50],'cellModel': 'CE_Template'} #65
netParams.popParams['PKCdM_LTB'] = {'cellType': 'LTB', 'numCells': 5, 'xRange':[55,100],'yRange':[0,50], 'cellModel': 'CE_Template'} #40
netParams.popParams['PKCdM_LF'] = {'cellType': 'LF', 'numCells': 5, 'xRange':[55,100],'yRange':[0,50], 'cellModel': 'CE_Template'} #15
netParams.popParams['PKCdP_RS'] = {'cellType': 'RS', 'numCells': 5, 'xRange':[55,100],'yRange':[0,50], 'cellModel': 'CE_Template'}
netParams.popParams['PKCdP_LTB'] = {'cellType': 'LTB', 'numCells': 5, 'xRange':[55,100], 'yRange':[0,50],'cellModel': 'CE_Template'}
netParams.popParams['PKCdP_LF'] = {'cellType': 'LF', 'numCells': 5, 'xRange':[55,100],'yRange':[0,50], 'cellModel': 'CE_Template'}
netParams.popParams['CeM_RS'] = {'cellType': 'RS', 'numCells': 5, 'xRange':[55,100],'yRange':[50,100], 'cellModel': 'CE_Template'} #70
netParams.popParams['CeM_LTB'] = {'cellType': 'LTB', 'numCells': 5, 'xRange':[55,100],'yRange':[50,100],'cellModel': 'CE_Template'} #185
netParams.popParams['CeM_LF'] = {'cellType': 'LF', 'numCells': 5, 'xRange':[55,100],'yRange':[50,100],'cellModel': 'CE_Template'} #5


## Synaptic mechanism parameters
#June15,2017 -- synapses don't seem to cause spiking, may need extra parameters. Check HOC files.
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 4, 'tau2': 10, 'e': 0}  # excitatory synaptic mechanism for noise

netParams.synMechParams['laf2CeLPKCDm'] = {'mod': 'laf2CeLPKCDm', 'initW':2.7} #LAf-->PKCdM
netParams.synMechParams['laf2CeLPKCDp'] = {'mod': 'laf2CeLPKCDp', 'initW':2.7} #LAf-->PKCdP
netParams.synMechParams['baf2CeLPKCDm'] = {'mod': 'baf2CeLPKCDm', 'initW':2.7} #BAf-->PKCdM
netParams.synMechParams['baf2CeLPKCDp'] = {'mod': 'baf2CeLPKCDp', 'initW':2.7} #BAf-->PKCdP
netParams.synMechParams['itcd2CeLPKCDm'] = {'mod': 'itcd2CeLPKCDm', 'initW':0.8} #ITCd-->PKCdM
netParams.synMechParams['itcd2CeLPKCDp'] = {'mod': 'itcd2CeLPKCDp', 'initW':0.8} #ITCd-->PKCdP
netParams.synMechParams['itcv2CeM'] = {'mod': 'itcv2CeM','initW':0.8} #ITCv-->CeM
netParams.synMechParams['baf2CeM'] = {'mod': 'baf2CeM','initW':2.5} #baf-->CeM
netParams.synMechParams['CeLPKCDm2CeM'] = {'mod': 'CeLPKCDm2CeM','initW':2} #PKCDm-->CeM
netParams.synMechParams['CeLPKCDp2CeM'] = {'mod': 'CeLPKCDp2CeM','initW':2} #PKCDp-->CeM
netParams.synMechParams['CeM2CeM'] = {'mod': 'CeM2CeM','initW':2.2} #CeM-->CeM
netParams.synMechParams['CeLPKCDm2CeLPKCDp'] = {'mod': 'CeLPKCDm2CeLPKCDp', 'initW':2.5}  # PKCDm-->PKCDp
netParams.synMechParams['CeLPKCDm2CeLPKCDm'] = {'mod': 'CeLPKCDm2CeLPKCDm', 'initW':1.5}  # PKCDm-->PKCDm
netParams.synMechParams['CeLPKCDp2CeLPKCDm'] = {'mod': 'CeLPKCDp2CeLPKCDm', 'initW':0.01}  # PKCDp-->PKCDm
netParams.synMechParams['CeLPKCDp2CeLPKCDp'] = {'mod': 'CeLPKCDp2CeLPKCDp', 'initW':3.5}  # PKCDp-->PKCDp

# Stimulation parameters

# Need to generate background noise 
netParams.stimSourceParams['bkg_PKCdM'] = {'type': 'NetStim', 'rate': 2, 'noise': 0.5}
netParams.stimSourceParams['bkg_PKCdP'] = {'type': 'NetStim', 'rate': 2, 'noise': 0.5}
netParams.stimSourceParams['bkg_CeM'] = {'type': 'NetStim', 'rate': 2.5, 'noise': 0.5}

#June15,2017 --- Tuned weights to elicit exactly one AP per stim
#June16,2017 --- Changed tau1 and tau2 above so weights may no longer be correct
#netParams.stimTargetParams['bkg->PKCdM_RS'] = {'source': 'bkg_PKCdM', 'conds': {'popLabel': 'PKCdM_RS'}, 'weight': 0.0026, 'delay': 0, 'synMech': 'exc'}
#netParams.stimTargetParams['bkg->PKCdM_LTB'] = {'source': 'bkg_PKCdM', 'conds': {'popLabel': 'PKCdM_LTB'}, 'weight': 0.005, 'delay': 0, 'synMech': 'exc'}
#etParams.stimTargetParams['bkg->PKCdM_LF'] = {'source': 'bkg_PKCdM', 'conds': {'popLabel': 'PKCdM_LF'}, 'weight': 0.009, 'delay': 0, 'synMech': 'exc'}
#netParams.stimTargetParams['bkg->PKCdP_RS'] = {'source': 'bkg_PKCdP', 'conds': {'popLabel': 'PKCdP_RS'}, 'weight': 0.0026, 'delay': 0, 'synMech': 'exc'}
#netParams.stimTargetParams['bkg->PKCdP_LTB'] = {'source': 'bkg_PKCdP', 'conds': {'popLabel': 'PKCdP_LTB'}, 'weight': 0.005, 'delay': 0, 'synMech': 'exc'}
#netParams.stimTargetParams['bkg->PKCdP_LF'] = {'source': 'bkg_PKCdP', 'conds': {'popLabel': 'PKCdP_LF'}, 'weight': 0.009, 'delay': 0, 'synMech': 'exc'}
#netParams.stimTargetParams['bkg->CeM_RS'] = {'source': 'bkg_CeM', 'conds': {'popLabel': 'CeM_RS'}, 'weight': 0.0026, 'delay': 0, 'synMech': 'exc'}
#netParams.stimTargetParams['bkg->CeM_LTB'] = {'source': 'bkg_CeM', 'conds': {'popLabel': 'CeM_LTB'}, 'weight': 0.005, 'delay': 0, 'synMech': 'exc'}
#netParams.stimTargetParams['bkg->CeM_LF'] = {'source': 'bkg_CeM', 'conds': {'popLabel': 'CeM_LF'}, 'weight':  0.009, 'delay': 0, 'synMech': 'exc'}

'''
# Use this to perform current clamp on cell types
netParams.stimSourceParams['c_clamp'] = {'type': 'IClamp', 'delay': 800, 'dur':2000, 'amp': -0.01}

duration = 1000
interval = int(1000/2)
num = (duration)/interval
netParams.stimSourceParams['c_stim'] = {'type': 'NetStim', 'delay':1200,'interval':interval,'number':num, 'noise':0}
netParams.stimTargetParams['IClamp->LTB'] = {'source': 'c_clamp', 'conds': {'cellType': 'LTB'}, 'sec':'soma', 'loc':0.5}
netParams.stimTargetParams['IClamp->RS'] = {'source': 'c_clamp', 'conds': {'cellType': 'RS'}, 'sec':'soma', 'loc':0.5}
netParams.stimTargetParams['IClamp->LF'] = {'source': 'c_clamp', 'conds': {'cellType': 'LF'}, 'sec':'soma', 'loc':0.5}
netParams.stimTargetParams['c_stim->RS'] = {'source': 'c_stim', 'conds':{'cellType':['RS','LTB']},'weight':  0.0026, 'delay': 0,'synMech':'exc'}
'''


## Cell connectivity rules
#Inputs-->PKCdM

netParams.connParams['LA->PKCdM'] = {'preConds': {'popLabel': ['LAf','LAer']}, 
	'postConds': {'popLabel': ['PKCdM_RS','PKCdM_LTB','PKCdM_LF']},
	'probability': .07, 			# probability of connection
	'weight': 1, 			# synaptic weight 
	'delay': random.uniform(2,5),					# transmission delay (ms) 
	'threshold':-10,
	'sec': 'adend',				# section to connect to
	'loc': 0.5,					# location of synapse
	'synMech': 'laf2CeLPKCDm'}   		# target synaptic mechanism
	

netParams.connParams['BA->PKCdM'] = {'preConds': {'popLabel': ['BAf','BAer']}, 
	'postConds': {'popLabel': ['PKCdM_RS','PKCdM_LTB','PKCdM_LF']},
	'probability': .07, 			# probability of connection
	'weight': 1, 			# synaptic weight 
	'delay': random.uniform(2,5),					# transmission delay (ms) 
	'threshold':-10,
	'sec': 'adend',				# section to connect to
	'loc': 0.5,					# location of synapse
	'synMech': 'baf2CeLPKCDm'}   		# target synaptic mechanism
'''
netParams.connParams['ITCd->PKCdM'] = {'preConds': {'popLabel': 'ITCd'}, 
	'postConds': {'popLabel': ['PKCdM_RS','PKCdM_LTB','PKCdM_LF']},
	'probability': 1, 			# probability of connection
	'weight': 1, 			# synaptic weight 
	'delay': 5,					# transmission delay (ms) 
	#'sec': 'adend',				# section to connect to
	#'loc': 0.5,					# location of synapse
	'synMech': 'itcd2CeLPKCDm'}   		# target synaptic mechanism

#Inputs-->PKCdP
netParams.connParams['LA->PKCdP'] = {'preConds': {'popLabel': ['LAf','LAer']}, 
	'postConds': {'popLabel': ['PKCdP_RS','PKCdP_LTB','PKCdP_LF']},
	'probability': .07, 			# probability of connection
	'weight': 1, 			# synaptic weight 
	'delay': 5,					# transmission delay (ms) 
	#'sec': 'adend',				# section to connect to
	#'loc': 0.5,					# location of synapse
	'synMech': 'laf2CeLPKCDp'}   		# target synaptic mechanism
	
netParams.connParams['BA->PKCdP'] = {'preConds': {'popLabel': ['BAf','BAer']}, 
	'postConds': {'popLabel': ['PKCdP_RS','PKCdP_LTB','PKCdP_LF']},
	'probability': .07, 			# probability of connection
	'weight': 1, 			# synaptic weight 
	'delay': 5,					# transmission delay (ms) 
	#'sec': 'adend',				# section to connect to
	#'loc': 0.5,					# location of synapse
	'synMech': 'baf2CeLPKCDp'}   		# target synaptic mechanism

netParams.connParams['ITCd->PKCdP'] = {'preConds': {'popLabel': 'ITCd'}, 
	'postConds': {'popLabel': ['PKCdP_RS','PKCdP_LTB','PKCdP_LF']},
	'probability': 1, 			# probability of connection
	'weight': 1, 			# synaptic weight 
	'delay': 5,					# transmission delay (ms) 
	#'sec': 'adend',				# section to connect to
	#'loc': 0.5,					# location of synapse
	'synMech': 'itcd2CeLPKCDp'}   		# target synaptic mechanism


## Inputs --> CeM
netParams.connParams['ITCv->CeM'] = {'preConds': {'popLabel': 'ITCv'}, 
	'postConds': {'popLabel': ['CeM_RS','CeM_LTB','CeM_LF']},
	'probability': .07, 			# probability of connection
	'weight': 0.7, 			# synaptic weight 
	'delay': 5,					# transmission delay (ms) 
	#'sec': 'adend',				# section to connect to
	#'loc': 0.5,					# location of synapse
	'synMech': 'itcv2CeM'}   		# target synaptic mechanism

netParams.connParams['BA->CeM'] = {'preConds': {'popLabel': ['BAf','BAer']}, 
	'postConds': {'popLabel': ['CeM_RS','CeM_LTB','CeM_LF']},
	'probability': .07, 			# probability of connection
	'weight': 1, 			# synaptic weight 
	'delay': 5,					# transmission delay (ms) 
	#'sec': 'adend',				# section to connect to
	#'loc': 0.5,					# location of synapse
	'synMech': 'baf2CeM'}   		# target synaptic mechanism


## Intrinsic Ce
netParams.connParams['PKCdM->PKCdP'] = {'preConds': {'popLabel': ['PKCdM_RS','PKCdM_LTB','PKCdM_LF']}, 
	'postConds': {'popLabel': ['PKCdP_RS','PKCdP_LTB','PKCdP_LF']},
	'probability': .04, 			# probability of connection
	'weight': 2.5, 			# synaptic weight 
	'delay': 5,					# transmission delay (ms) 
	#'sec': 'adend',				# section to connect to
	#'loc': 0.5,					# location of synapse
	'synMech': 'CeLPKCDm2CeLPKCDp'}   		# target synaptic mechanism

netParams.connParams['PKCdM->PKCdM'] = {'preConds': {'popLabel': ['PKCdM_RS','PKCdM_LTB','PKCdM_LF']}, 
	'postConds': {'popLabel': ['PKCdM_RS','PKCdM_LTB','PKCdM_LF']},
	'probability': .02, 			# probability of connection
	'weight': 2.5, 			# synaptic weight 
	'delay': 5,					# transmission delay (ms) 
	#'sec': 'adend',				# section to connect to
	#'loc': 0.5,					# location of synapse
	'synMech': 'CeLPKCDm2CeLPKCDm'}   		# target synaptic mechanism
	
netParams.connParams['PKCdP->PKCdM'] = {'preConds': {'popLabel': ['PKCdP_RS','PKCdP_LTB','PKCdP_LF']}, 
	'postConds': {'popLabel': ['PKCdM_RS','PKCdM_LTB','PKCdM_LF']},
	'probability': .01, 			# probability of connection
	'weight': 2.5, 			# synaptic weight 
	'delay': 5,					# transmission delay (ms) 
	#'sec': 'adend',				# section to connect to
	#'loc': 0.5,					# location of synapse
	'synMech': 'CeLPKCDp2CeLPKCDm'}   		# target synaptic mechanism
	
netParams.connParams['PKCdP->PKCdP'] = {'preConds': {'popLabel': ['PKCdP_RS','PKCdP_LTB','PKCdP_LF']}, 
	'postConds': {'popLabel': ['PKCdP_RS','PKCdP_LTB','PKCdP_LF']},
	'probability': .02, 			# probability of connection
	'weight': 2.5, 			# synaptic weight 
	'delay': 5,					# transmission delay (ms) 
	#'sec': 'adend',				# section to connect to
	#'loc': 0.5,					# location of synapse
	'synMech': 'CeLPKCDp2CeLPKCDp'}   		# target synaptic mechanism
	
netParams.connParams['PKCdP->CeM'] = {'preConds': {'popLabel': ['PKCdP_RS','PKCdP_LTB','PKCdP_LF']}, 
	'postConds': {'popLabel': ['CeM_RS','CeM_LTB','CeM_LF']},
	'probability': .05, 			# probability of connection
	'weight': 2.5, 			# synaptic weight 
	'delay': 5,					# transmission delay (ms) 
	#'sec': 'adend',				# section to connect to
	#'loc': 0.5,					# location of synapse
	'synMech': 'CeLPKCDp2CeM'}   		# target synaptic mechanism
	
netParams.connParams['PKCdM->CeM'] = {'preConds': {'popLabel': ['PKCdM_RS','PKCdM_LTB','PKCdM_LF']}, 
	'postConds': {'popLabel': ['CeM_RS','CeM_LTB','CeM_LF']},
	'probability': .01, 			# probability of connection
	'weight': 2.5, 			# synaptic weight 
	'delay': 5,					# transmission delay (ms) 
	#'sec': 'adend',				# section to connect to
	#'loc': 0.5,					# location of synapse
	'synMech': 'CeLPKCDm2CeM'}   		# target synaptic mechanism
	
netParams.connParams['CeM->CeM'] = {'preConds': {'popLabel': ['CeM_RS','CeM_LTB','CeM_LF']}, 
	'postConds': {'popLabel': ['CeM_RS','CeM_LTB','CeM_LF']},
	'probability': .02, 			# probability of connection
	'weight': 2.5, 			# synaptic weight 
	'delay': 5,					# transmission delay (ms) 
	#'sec': 'adend',				# section to connect to
	#'loc': 0.5,					# location of synapse
	'synMech': 'CeM2CeM'}   		# target synaptic mechanism
'''



# Simulation options
simConfig = specs.SimConfig()		# object of class SimConfig to store simulation configuration

simConfig.duration = 3000 			# Duration of the simulation, in ms
simConfig.dt = 0.025 				# Internal integration timestep to use
simConfig.verbose = False  			# Show detailed messages 
simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
simConfig.recordStep = 0.25 			# Step size in ms to save data (eg. V traces, LFP, etc)
simConfig.filename = 'model_output'  # Set file output name

simConfig.saveMat = False 		# Save params, network a sim output to pickle file
simConfig.analysis['plotRaster'] = True# Plot a raster
simConfig.analysis['plotTraces'] = {'include': [81, 86, 91]} 			# Plot recorded traces for this list of cells
simConfig.analysis['plot2Dnet']  = True         # plot 2D visualization of cell positions and connections
#simConfig.analysis['plotConn'] = {'feature':'numConns'}
simConfig.timestampFilename = True
# Create network and run simulation
sim.createSimulateAnalyze(netParams, simConfig)
#sim.simulate()
#sim.saveData()
#for i in range(1, 4):
#	simConfig.filename = 'Run' + str(i)
#	sim.net.modifySynMechs({'label':'laf2CeLPKCDm', 'initW': 2.7*(i)})
#	sim.simulate()
#	sim.saveData()

import pylab; pylab.show()  # this line is only necessary in certain systems where figures appear empty