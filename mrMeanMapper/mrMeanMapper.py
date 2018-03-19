import sys
from numpy import *
def read_input(file):
    for line in file:
        yield line.rstrip()

input= read_input(sys.stdin)
input=[float(line) for line in input]
#print(input)
numInputs =len(input)
input =mat(input)
sqInput =power(input,2)
#print(sqInput)
print("%d \t %f \t %f" %(numInputs,input.mean(),sqInput.mean()))
print( sys.stderr,"report:still alive")
