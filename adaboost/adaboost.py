from numpy import *
def loadSimpData():
    datMat =matrix([[1.,2.1],
                    [2.,1.1],
                    [1.3,1.],
                    [1.,1.],
                    [2.,1.]])
    classLabels =[1.0,1.0,-1.0,-1.0,1.0]
    return datMat ,classLabels
def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):
    retArray =ones((shape(dataMatrix)[0],1))
    if threshIneq =='lt':
        retArray[dataMatrix[:,dimen]<=threshVal]= -1.0
    else:
        retArray[dataMatrix[:,dimen]>threshVal]= -1.0
    return retArray
def buildStump(dataArr,classLabels,D):
    dataMatrix =mat(dataArr); labelMat =mat(classLabels).T
    m,n =shape(dataMatrix)
    numSteps =10.0 ; bestStump ={}; bestClasEst =mat(zeros((m,1)))
    minError =inf
    for i in range(n):
        rangeMin = dataMatrix[:,i].min() ; rangeMax =dataMatrix[:,i].max()
        stepSize =(rangeMax-rangeMin)/numSteps
        for j in range(-1,int(numSteps)+1):
            for inequal in ['lt','rt']:
                threshVal = (rangeMin+float(j)*stepSize)
                predictedVals =stumpClassify(dataMatrix,i,threshVal,inequal)
                errArr =mat(ones((m,1)))
                errArr[predictedVals ==labelMat]=0
                weightedError =D.T*errArr
                print("split:dim %d ,thresh %.2f ,thresh ineqal:%s ,the weighted error is %.3f" %(i,threshVal,inequal,weightedError))
                if weightedError < minError:
                    minError =weightedError
                    bestClasEst =predictedVals.copy()
                    bestStump['dim'] =i
                    bestStump['thresh'] =threshVal
                    bestStump['ineq']= inequal
    return bestStump , minError , bestClasEst
#完整的AdaBoost算法实现
def adaBoostTrainDS(dataArr,classLabels,numIt=40):
    weakClassArr =[]
    m=shape(dataArr)[0]
    D=mat(ones((m,1))/m)#权重向量
    aggClassEst =mat(zeros((m,1)))
    for i in range(numIt):
        bestStump,error,classEst =buildStump(dataArr,classLabels,D)
        print("D:",D.T)
        alpha =float(0.5*log((1.0-error)/max(error,1e-16)))
        bestStump['alpha']=alpha
        weakClassArr.append(bestStump)
        print("classEst:",classEst.T)
        expon =multiply(-1*alpha*mat(classLabels).T,classEst)#正确分类前面加负号，错误分类正号
        #print(shape(expon))#相乘
        D =multiply(D,exp(expon))
        D=D/D.sum()
        aggClassEst +=alpha*classEst#权重与每一次分类结果向量相乘
        print("aggClassEst:",aggClassEst.T)
        aggErrors =multiply(sign(aggClassEst)!=mat(classLabels).T,ones((m,1)))#sign表示正数为1，负数为-1
        errorRate =aggErrors.sum()/m
        print("total error:" ,errorRate,"\n")
        if errorRate ==0.0: break
    return weakClassArr,aggClassEst
#测试算法：基于AdaBoost的分类
def adaClassify(datToClass,classifierArr):#datToClass是待分类样本点
    dataMatrix =mat(datToClass)
    m =shape(dataMatrix)[0]
    aggClassEst =mat(zeros((m,1)))
    for i in range(len(classifierArr)):
        classEst =stumpClassify(dataMatrix,classifierArr[i]['dim'],\
                                classifierArr[i]['thresh'],\
                                classifierArr[i]['ineq'])
        aggClassEst +=classifierArr[i]['alpha']*classEst
        print(aggClassEst)
    return sign(aggClassEst)
#示例：在一个难数据集上应用AdaBoost
#自适应数据加载函数
def loadDataSet(fileName):
    numFeat =len(open(fileName).readline().split('\t'))
    dataMat =[]; labelMat=[]
    fr =open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine =line.strip().split('\t')
        for i in range(numFeat-1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat
def plotROC(predStrengths, classLabels):
    '''import matplotlib.pyplot as plt
    cur =(0.0,0.0)
    numstep=1/len(predStrengths)
    sortedIndicies =predStrengths.argsort()
    #print(sortedIndicies)
    predStrengths2=sign(sort(predStrengths.tolist()[0]))
    #print(predStrengths2)
    fig =plt.figure()
    fig.clf()
    ax=plt.subplot()
    tn=fn=tp=fp=0
    Ratetp=Ratefp=0
    sum=0.0
    #Ratefp =fp/(fp+tn)
    for index in sortedIndicies.tolist()[0]:
        if classLabels[index] ==list(predStrengths2)[index]:
            if classLabels[index]==-1:
                tn +=1
                #print(tn)
            else:
                tp+=1
                #print(tp)
        else:
            if classLabels[index]==-1:
                fp+=1
                #print(fp)
            else :
                fn +=1
        print(fp,tp,fn,tn)        #print(fn)
        if fp+tn==0 or fn+tp==0:
            continue
        Ratefp =fp/(fp+tn)
        Ratetp =tp/(tp+fn)
        print(Ratefp,Ratetp)
        sum+=Ratetp*numstep
        ax.scatter(Ratefp,Ratetp,c='b')
    ax.plot([0, 1], [0, 1], 'b--')
    plt.xlabel('False Position Rate')
    plt.ylabel('True Position Rate')
    plt.title('ROC curve for AdaBoost Horse Colic Detection System')
    ax.axis([0, 1, 0, 1])
    plt.show()
    print('the Area Under the curve is:', sum)
    return (sortedIndicies)
    '''
    import matplotlib.pyplot as plt
    cur =(1.0,1.0)
    ySum =0.0
    numPosClas =sum(array(classLabels)==1.0)
    print(numPosClas,len(classLabels-numPosClas))
    yStep =1/float(numPosClas)#真实结果中的正例步长
    xStep =1/float(len(classLabels)-numPosClas)#真实结果中的反例步长
    print(xStep,yStep)
    sortedIndicies =predStrengths.argsort()
    print(sortedIndicies)
    fig =plt.figure()
    fig.clf()
    ax =plt.subplot(111)
    for index in sortedIndicies.tolist()[0]:
        if classLabels[index] ==1.0:
            delX =0;delY =yStep
        else :
            delX =xStep; delY= 0
            ySum +=cur[1]
        ax.scatter([cur[0]-delX],[cur[1]-delY],c='b')
        cur =(cur[0]-delX,cur[1]-delY)
        #print(cur[0]-delX,cur[1]-delY)
    ax.plot([0,1],[0,1],'b--')
    plt.xlabel('False Position Rate'); plt.ylabel('True Position Rate')
    plt.title('ROC curve for AdaBoost Horse Colic Detection System')
    ax.axis([0,1,0,1])
    plt.show()
    print('the Area Under the curve is:',ySum*xStep)
    return(sortedIndicies)
    '''
def plotROC(predStrengths, classLabels):
    import matplotlib.pyplot as plt
    cur =(1.0,1.0)
    ySum =0.0
    numPosClas =sum(array(classLabels)==1.0)
    print(numPosClas)
    yStep =1/float(numPosClas)
    xStep =1/float(len(classLabels-numPosClas))
    sortedIndicies =(predStrengths.T>0).argsort()
    print(sortedIndicies)
    fig =plt.figure()
    fig.clf()
    ax =plt.subplot(111)
    for index in sortedIndicies.tolist()[0]:
        if classLabels[index] ==1.0:
            delX = xStep;delY =0
        else :
            delX =xStep; delY= yStep
        ySum +=cur[1]
        ax.plot([cur[0],cur[0]-delX],[cur[1],cur[1]-delY],c='b')
        cur =(cur[0]-delX,cur[1]-delY)
        #print(cur[0]-delX,cur[1]-delY)
    ax.plot([0,1],[0,1],'b--')
    plt.xlabel('False Position Rate'); plt.ylabel('True Position Rate')
    plt.title('ROC curve for AdaBoost Horse Colic Detection System')
    ax.axis([0,1,0,1])
    plt.show()
    print('the Area Under the curve is:',ySum*xStep)
    return(sortedIndicies)
'''
