

LAf=[]
for i in range(1,21):
	file = open('Data_Input/Input_laf{}.dat'.format(i)) #Import our input files 
	LAf.append(file.read().splitlines())
	LAf[i-1]=map(float,LAf[i-1]) #This is needed to convert from strings to numbers
print LAf[-1]