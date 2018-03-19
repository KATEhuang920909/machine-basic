from numpy import *
def standEst(dataMat,user,simMeas,item):
    n=shape(dataMat)[1]
    simTotal=0.0;ratSimTotal =0.0
    for j in range(n):
        userRating =dataMat[user,j]
        if userRating ==0: continue
        overLap=nonzero(logical_and(dataMat[:,item].A>0,dataMat[:,j].A>0))[0]#已被评论的元素
        if len(overLap) ==0: similarity =0
        else: similarity =simMeas(dataMat[overLap,item],dataMat[overLap,j])#overLap为列表
        print('the %d and %d similarity is : %f' %(item,j,similarity))
        simTotal+=similarity
        ratSimTotal+=similarity*userRating
    if simTotal ==0: return 0
    else: return ratSimTotal/simTotal