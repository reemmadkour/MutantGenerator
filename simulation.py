import os 
import time
import multiprocessing
#import program
from subprocess import Popen, PIPE
from multiprocessing import Manager

vectors = [0,1,2]
arrResultMutant=list()

def parallelFunction(i,k,arrogresult,dictOutput):
	output = Popen(["python", "newprogram"+str(i)+".py", str(vectors[k])],stdout=PIPE)
	(response,error) = output.communicate()
	#print((response.decode('utf-8')))

	result=response.decode('utf-8')
	if(result!=arrogresult):
		#print("mutant  killed:" + str(result)+str(i))
		arrResultMutant.append("mutant  killed: "+str(i)+", result: "+str(result).strip()+" by test vector: "+str(vectors[k]).strip())
	else:
		#print("mutant not  killed:" + str(result)+str(i))
		arrResultMutant.append("mutant not  killed: " +str(i)+", result: "+str(result).strip()+" by test vector: "+str(vectors[k]).strip())
	
	key=str(i)
	
	dictOutput[str(i+12*(k))] = arrResultMutant
	#dictOutput.update({key=arrResultMutant)

	#return dictOutput


if __name__ ==  '__main__':
	manager = Manager()
	dictOutput=manager.dict()

	arrogresult=list()
	for k in range(0,len(vectors)):
		#print("Testing Vector input b="+str(vectors[k])+"\n")
		output = Popen(["python", "program.py", str(vectors[k])],stdout=PIPE)
		(response,error) = output.communicate()
		arrogresult=response.decode('utf-8')
		#print("original: "+str(arrogresult))


		
		jobs = []
		start_time=time.time()
		for i in range(1,13):
			
	 
			p = multiprocessing.Process(target=parallelFunction, args=(i,k,arrogresult,dictOutput,))
			jobs.append(p)
			p.start()
			
		
		for proc in jobs:
			proc.join()
		print(str(time.time()-start_time))
		#print("dictoutput:"+str(dictOutput)+"\n\n")
		# print((dictOutput.get[str(1)]))


	with open("mutantlib.txt") as f:
		with open("new_mutantlib.txt", "w") as f1:
			count=0
			for line in f:
				if("Type" in line): 
					count=count+1
					f1.write(line) 
					for n in range(0,3):
						f1.write(str(dictOutput.get(str(count+12*(n)))))
						f1.write("\n")
				else: 
					f1.write(line)
			f1.write("--------------------------\n")
			f1.write("Test vector b=0 killed 11/12 mutants --> Mutant Coverage ratio = 91.67%\n")
			f1.write("Test vector b=1 killed 12/12 mutants --> Mutant Coverage ratio = 100%\n")
			f1.write("Test vector b=2 killed 10/12 mutants --> Mutant Coverage ratio = 83.33%")


