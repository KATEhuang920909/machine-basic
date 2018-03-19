from numpy import  *
def loadDataSet(fileName,delim='\t'):
    fr =open(fileName)
    stringArr=[line.strip().split(delim) for line in fr.readlines()]
    datArr= [list(map(float,line) )for line in stringArr]
    return mat(datArr)
def pca(datMat,topNfeat =9999999):
    meanVals =mean(datMat,axis=0)#列
    meanRemoved =datMat -meanVals
    covMat=cov(meanRemoved ,rowvar=False)#列为特征维
    eigVals ,eigVects=linalg.eig(mat(covMat))
    eigValInd =argsort(eigVals)
    eigValInd =eigValInd[:-(topNfeat+1):-1]#
    redEigVects= eigVects[:,eigValInd]
    lowDDataMat =meanRemoved * redEigVects
    reconMat =(lowDDataMat *redEigVects.T)+meanVals
    return lowDDataMat ,reconMat
#示例：利用PCA对半导体制造数据降维
def replaceNanWithMean():
    datMat=loadDataSet(r'secom.data',' ')
    numFeat=shape(datMat)[1]
    for i in range(numFeat):
        meanVal =mean(datMat[nonzero(~isnan(datMat[:,i].A))[0],i])
        datMat[nonzero(isnan(datMat[:,i].A))[0],i]=meanVal

    return  datMat