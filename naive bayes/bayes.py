# -*- coding: utf-8 -*-
def  loadDataSet():
    postingList=[['my','dog','has','flea',\
                  'problems','help','please'],
                 ['maybe','not','take','him',\
                  'to','dog','park','stupid'],
                 ['my','dalmation','is','so','cute',\
                  'I','love','him'],
                 ['stop','posting','stupid','worthless','garbage'],
                 ['mr','licks','ate','my','steak','how',\
                  'to','stop','him'],
                 ['quit','buying','worthless','dog','food','stupid']]
    classVec =[0,1,0,1,0,1]
    return postingList,classVec
def createVocabList (dataSet):
    vocabSet =set([])
    for document in dataSet:
        vocabSet =vocabSet | set(document)
    return list(vocabSet)
def setofWord2Vec(vocabList ,inputSet):
    returnVec= [0]*len(vocabList)
    for word in inputSet:
        #if word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else:
            print("the word: %s is not in my Vocabulary!" %word)
    return returnVec
def trainNB0(trainMatrix,trainCategory):
    import numpy as np
    numTrainDocs =len(trainMatrix)
    numWords =len(trainMatrix[0])

    pAbusive =sum(trainCategory)/float(numTrainDocs)
    p0Num =np.ones(numWords)# numpy.zeros(numWords)
    p1Num =np.ones(numWords)#numpy.zeros(numWords)
    #p0Num = numpy.zeros(numWords)
    #p1Num= numpy.zeros(numWords)
    p0Denom =2.0 ;p1Denom =2.0
    for i in range(numTrainDocs):
        if trainCategory[i]==1:
            p1Num +=trainMatrix[i]
            p1Denom +=sum(trainMatrix[i])
        else:
            p0Num +=trainMatrix[i]
            p0Denom +=sum(trainMatrix[i])
    p1Vect =np.log(p1Num/p1Denom)#p1Num/p1Denom#p1Vect和P0Vect均为向量矩阵
    p0Vect =np.log(p0Num/p0Denom)#p0Num/p0Denom
    return p0Vect,p1Vect,pAbusive
def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1=sum(vec2Classify*p1Vec)+np.log(pClass1)
    p0=sum(vec2Classify*p0Vec)+np.log(1.0-pClass1)
    #print(p1,p0)
    if p1>p0:
        return 1
    else:
        return 0

def testingNB():
    listOPosts,listClasses =loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setofWord2Vec(myVocabList,postinDoc))
    p0V,p1V,pAb =trainNB0(trainMat,listClasses)
    testEntry =['love','my','dalmation']
    thisDoc =setofWord2Vec(myVocabList,testEntry)
    #print(thisDoc)
    print(testEntry,'classify as:',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = setofWord2Vec(myVocabList, testEntry)
    #print(thisDoc)
    print(testEntry, 'classify as:', classifyNB(thisDoc, p0V, p1V, pAb))
#listOPosts,listClass =loadDataSet()
#myVocabList=createVocabList(listOPosts)
#a=setofWord2Vec(myVocabList,listOPosts[0])
#print(a)
#navie bayes的词袋模型
def bagodWords2VecMN(vocabList,inputSet):
    returnVec =[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList,index(word)] +=1

#事例：使用朴素贝叶斯过滤垃圾邮件
#测试算法：使用朴素贝叶斯进行交叉验证
def textParse(bigString):
    import re

    listOfTokens= re.split('\W',bigString)
    return [tok.lower() for tok in listOfTokens if len(tok)>2]
def spamTest():
    import os
    import numpy as np
    os.chdir(r'H:\自学项目\机器学习\machinelearninginaction\Ch04\email')
    docList =[]; classList=[]; fullText =[]
    for i in range(1,26):
        wordList =textParse(open('spam/%d.txt'%i ).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList =textParse(open('ham/%d.txt'%i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    #print(docList,classList)
    vocabList =createVocabList(docList)
    trainingSet =list(range(50)); testSet =[]
    for i in range(10):#训练集40个，测试集10个
        randIndex =int(np.random.uniform(0,len(trainingSet)))#在0,len(trainingSet)之间随机生成一个数
        #print(randIndex)
        testSet.append(trainingSet[randIndex])
        del (trainingSet[randIndex])
        #del(classList[randIndex])
    trainMat=[]; trainClasses =[]
    for docIndex in trainingSet:
        trainMat.append(setofWord2Vec(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0v,p1v,pSpam =trainNB0(trainMat,trainClasses)
    errorcount =0
    for docIndex in testSet:
        wordVector =setofWord2Vec(vocabList,docList[docIndex])
        if classifyNB(wordVector,p0v,p1v,pSpam) !=classList[docIndex]:
            errorcount+=1
    print('the error rate is :',float(errorcount)/len(testSet))
#事例：使用朴素贝叶斯分类器从个人广告中获取区域倾向
##def calcMostFreq(vocabList,fullText):
#     import operator
#     freqDict ={}
#     for token in vocabList:
#         freq