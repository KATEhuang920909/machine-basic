from numpy import *
from tkinker import *
import regtrees
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import  Figure
def reDraw(tolS,tolN):
    reDraw.f.clf()
    reDraw.a =reDraw.f.add_subplot(111)
    if chkBtnVar.get():
        if tolN<2:tolN=2
        myTree =regtrees.createTree(reDraw.rawDat,regtrees.modelLeaf,regtrees.modelErr,(tolS,tolN))
        yHat =regtrees.createForeCast(myTree,reDraw.testDat,regtrees.modelTreeEval)
    else:
        myTree =regtrees.createTree(reDraw.rawDat,ops =(tolS,tolN))
        yHat = regtrees.createForeCast(myTree, reDraw.testDat)
    reDraw.a.scatter(reDraw.rawDat[:,0],reDraw.rawDat[:,1],s=5)
    reDraw.a.plot(reDraw.testDat,yHat,linewidth=2.0)
    reDraw.canvas.show()
def getInputs():
    try: tolN =int(tolNentry.get())
    except:
        tolN =10
        print("enter interger for tolN")
        tolNentry.delete(0,END)
        tolNentry.insert(0,'10')
    try: tolS =float(tolSentry.get())
    except:
        tolS=1.0
        print("enter Float for tols")
        tolNentry.delete(0, END)
        tolNentry.insert(0, '1.0')
    return tolN,tolS
def drawNewTree():
    tolN ,tolS =getInputs()
    reDraw(tolS,tolN)
rook =Tk()
'''Label(root,text="Plot Place Holder").grid(row=0,columnspan=3)
Label(root,text="tolN").grid(row=1,column=0)'''
reDraw.f =Figure(figsize=(5,4),dpi=100)
reDraw.canvas =FigureCanvasTkAgg(reDraw.f ,master =root)
reDraw.canvas.show()
reDraw.canvas.get_tk_widget().grid(row=0,columnspan=3)
tolNentry =Entry(root)
tolNentry.grid(row=1,columns =1)
tolNentry.insert(0,'10')
Label(root,text="tolS").grid(row=2,cloumns=0)
tolSentry =Entry(root)
tolSentry.grid(row=2,column=1)
tolSentry.insert(0,'1.0')
Button(root,text="ReDraw",command =drawNewTree).grid(row=1,column=2,rowspan =3)
chkBtnVar =IntVar()
chkBtn =Checkbutton(root,text="Model Tree",variable =chkBtnVar)
chkBtn.grid(row=3,column=0,columnspan =2)
reDraw(1.0,10)
root.mainloop()
