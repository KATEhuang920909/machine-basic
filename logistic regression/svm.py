def loadDataSet(fileName):
    dataMat =[] ; labelMat =[]
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =line.strip().split('\t')
        dataMat.append([float(lineArr[0]),float((lineArr[1]))])