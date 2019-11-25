import os 
#import program
from subprocess import Popen, PIPE
vectors = [0,1,2]
arrogresult=list()
for k in range(0,len(vectors)):
	print("Testing Vector input b="+str(vectors[k])+"\n")
	output = Popen(["python", "program.py", str(vectors[k])],stdout=PIPE)
	(response,error) = output.communicate()
	arrogresult=response.decode('utf-8')
	print("original: "+str(arrogresult))


	arrResultMutant=list()

	for i in range(1,12):

		output = Popen(["python", "newprogram"+str(i)+".py", str(vectors[k])],stdout=PIPE)
		(response,error) = output.communicate()
		#print((response.decode('utf-8')))
		arrResultMutant.append(response.decode('utf-8'))
		result=response.decode('utf-8')
		if(result!=arrogresult):
			print("mutant  killed:" + str(result)+str(i))
		else:
			print("mutant not  killed:" + str(result)+str(i))



#os.system('python program.py 2')