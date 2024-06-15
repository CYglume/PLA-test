import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

class PLAPercep:
    def __init__(self, dtIN):
        self.dt = dtIN
        self.colorID = 1

    def colorSet(self):
        if self.colorID == 1:
            color = self.dt.col.map({-1: 'red', 1: 'blue'})
        return(color)

    def ClasPlot(self, W, i, org):
        # classification function: y = y_o + m(x-x_o)
        #                          0 = mx - y + (y_0 - mx_0)
        a = W[0]
        b = W[1]
        slp = -a/b
        x = np.arange(-21, 21, 0.01)
        yM = 21
        ym = -21
        print('W = {}'.format([a,b]))
        print('slope = {}'.format(slp))
        y1 = slp*(x - org[0]) + org[1]
        
        plt.subplot(3, 4, i+1)
        plt.scatter(self.dt.x,self.dt.y, c = self.colorSet())
        plt.axline(xy1=org, slope=-(a/b),
                   linestyle = '--', )
        plt.fill_between(x, y1, yM, facecolor = 'blue', alpha = 0.3)
        plt.fill_between(x, y1, ym, facecolor = 'red', alpha = 0.3)
        plt.xlim(-21,21)
        plt.ylim(-21,21)
        plt.title("Iter " + str(i+1))


        #Chekc the match to pre-classification
        fit = slp*self.dt.x - self.dt.y + (org[1] - slp*org[0])
        wrongList = np.sign(fit) == self.dt.col
        wrongDist = abs(fit * wrongList)

        #see if complete classification
        if not any(wrongList):
            return(0,0)

        #Get the farthest point in the wrong side
        wrongDT = self.dt[wrongDist == max(wrongDist)]


        Xt = np.array(wrongDT.iloc[0,[0,1]])
        yn = wrongDT.iloc[0,2]
        Wt = W + Xt * yn
        print('||||----||||')
        print(Xt)
        print('kkkkkkkkkkkkkk')
        print(W)
        print(yn)
        print('||||----||||')
        return(Wt, yn)


    def PLA(self, iter = 11):
        org = [self.dt.x.mean(), self.dt.y.mean()]
        W   = [org[0] - self.dt.x[1], org[1] - self.dt.y[1]]
        yn  = 1
        i   = 0
        for i in range(iter):
            W, yn = self.ClasPlot(W, i, org)
            print('W = {}'.format(W))
            print('yn = {}'.format(yn))
            print('i = {}'.format(i))
            print('----')
            if (yn == 0):
                print('End!')
                break
        
        plt.subplots_adjust(hspace=0.5)
        plt.suptitle("Subplot Test")
        plt.show()


if __name__ == "__main__":
    PLAobj = PLAPercep(trainDT)