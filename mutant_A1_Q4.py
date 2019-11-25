import pandas as pd

arr = ["+", "-","/","*"]
f= open("mutantlib.txt","w+")
linecount=0;
numMutantplus=0;
numMutantminus=0;
numMutantmultp=0;
numMutantdiv=0;
with open('program.py') as my_file:
	for line in my_file:
		linecount=linecount+1
		for x in arr :
			if(x in line):
				for y in arr:
					if(y!=x):
						f.write( "Line number= "+str(linecount)+"\n")
					
						f.write("Original exp:"+x+"\n")
						f.write("Type:"+ y+"\n")
						f.write("--------------------------\n")
						if(y=="*"):
							numMutantmultp=numMutantmultp+1
						if(y=="+"):
							numMutantplus=numMutantplus+1
						if(y=="-"):
							numMutantminus=numMutantminus+1
						if(y=="/"):
							numMutantdiv=numMutantdiv+1
f.write("Number of + mutants: "+ str(numMutantplus)+"\n")
f.write("Number of - mutants: "+ str(numMutantminus)+"\n")
f.write("Number of * mutants: "+ str(numMutantmultp)+"\n")
f.write("Number of / mutants: "+ str(numMutantdiv)+"\n")

		
