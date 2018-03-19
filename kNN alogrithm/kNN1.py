from numpy import *
import operator
from os import listdir
import matplotlib
import matplotlib.pyplot as plt
def classify0(inX, dataSet, labels, k):#返回最近值标签
    dataSetSize = dataSet.shape[0]#第一维的长度
    diffMat = tile(inX, (dataSetSize,1)) - dataSet #tile 重复inx矩阵，次数为dataSetSize,构成列矩阵
    sqDiffMat = diffMat**2#幂运算
    sqDistances = sqDiffMat.sum(axis=1)#每一行向量相加
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort() #将distances从小到大排列，输出其索引    
    classCount={}   #定义集合       
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]#贴上标签
        classCount[voteIlabel]= classCount.get(voteIlabel,0)+1
    keys = classCount.keys()
    vals =classCount.values()
    lst =[(key,val) for key ,val in zip(keys,vals)]
    l=sorted(lst, key=operator.itemgetter(1), reverse=True)#以二维序列的第二个元素做逆排序
    return l[0][0]
def createDataSet():#实例
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def file2matrix(filename):#读取文件，并进行处理
	fr =open(filename)
	arrayOLines=fr.readlines()#读出每一行
	numberOfLines=len(arrayOLines)
	returnMat =zeros((numberOfLines,3))#构建总大小为numberOfLines的长度为3的一维零矩阵
	classLabelVector =[]#建立一个空序列
	index=0
	for line in arrayOLines:
		line =line.strip()#删除开头和结尾的空格等
		listFromLine =line.split('\t')#以空格形式分割，并以序列的形式返回
		returnMat[index]=listFromLine[0:3]#将returnMat矩阵重新赋值
		classLabelVector.append(int(listFromLine[-1]))#评价结果储存
		index +=1
	return returnMat,classLabelVector#返回
def autoNorm(dataSet):#归一化数值，并返回
	minVals = dataSet.min(0)#取列的最值构成数组
	maxVals = dataSet.max(0)
	ranges =maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges,minVals
def datingClassTest():#测试
	hoRatio =0.1
	datingDataMat,datingLabels =file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals =autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m*hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],5)
		print(classifierResult)
		print('the classifier came back with : {},the real answer is: {}'.format (classifierResult,datingLabels[i]))
		if (classifierResult != datingLabels[i]): errorCount +=1.0
	print("the total error rate is :%f" % (errorCount/float(numTestVecs)))
	print (errorCount)
def classifyPerson():#预测
	resultList = ['not at all' , 'in small doses','in large doses']
	percentTats = float(input("percentage of time spent playing video games?"))
	ffMiles = float(input("frequent fliters of ice cream consumed per year?"))
	iceCream = float(input("liters of ice cream consumed per year?"))
	datingDataMat ,datingLabels = file2matrix('datingTestSet2.txt')
	normMat,ranges ,minVals = autoNorm(datingDataMat)
	inArr = array([ffMiles,percentTats,iceCream])
	classifierResult = classify0((inArr - minVals)/ranges,normMat,datingLabels,3)
	print("you will probably like this person:", resultList[classifierResult-1])
#手写识别系统
def img2vector(filename):
	returnVect =zeros((1,1024))#一行，1024列零矩阵
	fr = open(filename)
	for i in range(32):
		lineStr =fr.readline()#读取一行，和readlines的区别？
		for j in range(32):
			returnVect[0,32*i+j] = int(lineStr[j])#每一行前32个数字存储于returnVect中
	return returnVect
def handwritingClassTest():
	hwLabels = []#构造空序列
	trainingFileList = listdir('trainingDigits')#获取文件目录
	m= len(trainingFileList)
	trainingMat = zeros((m,1024))#m行，1024列
	for i in range(m):
		fileNameStr = trainingFileList[i]
		fileStr = fileNameStr.split('.')[0]#分割文件名
		classNumStr = int(fileStr.split('_')[0])#分割文件名
		hwLabels.append(classNumStr)#增加到序列里\
		trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
	testFileList = listdir('testDigits')
	errorCount=0.0
	mTest = len(testFileList)
	print(mTest)
	lst=[]
	lst1=[(k) for k in range(0,10)]#0-99
	print(lst1)
	for j in range(1,10):
		for i in range(mTest):
			fileNameStr = testFileList[i]
			fileStr = fileNameStr.split('.')[0]
			classNumStr = int (fileStr.split('_')[0])
			vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
			classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels,lst1[j])
			print('the classifier came back with: {},the real answer is: {}'.format(classifierResult,classNumStr))
			if (classifierResult != classNumStr):
				errorCount +=1.0
		lst.append(errorCount/float(mTest))
		print(lst)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(lst1[1:10],lst)
	plt.show()
handwritingClassTest()