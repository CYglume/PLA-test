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

    def ClasPlot(self,W,i):
        # classification function: ax + by =0
        a = W[0]
        b = W[1]
        x = np.arange(-21, 21, 0.01)
        yM = 21
        ym = -21
        print(a)
        print(b)
        print('slope = {}'.format(-a/b))
        y1 = -(a/b)*x
        y1[(y1<ym)] = ym
        y1[(y1>yM)] = yM
        
        # p1 = plt.plot(self.dt.x,self.dt.y, c = col1)
        plt.scatter(self.dt.x,self.dt.y, c = self.colorSet())
        plt.axline(xy1=(0,0), slope=-(a/b),
                   linestyle = '--', )
        plt.fill_between(x, y1, yM, facecolor = 'blue', alpha = 0.3)
        plt.fill_between(x, y1, ym, facecolor = 'red', alpha = 0.3)
        plt.text(-20, 20, 'i = %i'%(i), fontsize = 22)
        plt.xlim(-21,21)
        plt.ylim(-21,21)
        plt.show()

        #Chekc the match to pre-classification
        fit = a*self.dt.x + b*self.dt.y
        chekcList = np.sign(fit) != self.dt.col
        
        #see if complete classification
        if not any(chekcList == False):
            return(0,0)

        #sample one data from incorrect classification
        ids = np.where(chekcList)[0].tolist()
        idGet = random.sample(ids, 1)
        
        Xt = np.array([self.dt.x[idGet].item(), self.dt.y[idGet].item()])
        yn = self.dt.col[idGet].item()
        Wt = W + Xt * yn
        print('||||----||||')
        print(Xt)
        print(W + Xt)
        print(Wt,yn)
        print('||||----||||')
        return(Wt, yn)


    def PLA(self):
        W = [self.dt.x[1], self.dt.y[1]]
        yn = 1
        i = 0
        while (yn) != 0:
            W, yn = self.ClasPlot(W, i)
            print('W = {}'.format(W))
            print('yn = {}'.format(yn))
            print('i = {}'.format(i))
            print('----')
            i += 1
            if i > 11:
                break

if __name__ == "__main__":
    PLAobj = PLAPercep(trainDT)