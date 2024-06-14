import PLA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def constructXY(org, radi, labelIn):
    angles = np.random.randint(360, size=(1,20))
    x = np.array(radi*np.cos(np.pi*angles/180), dtype=float)
    x+=org
    
    y = np.array(radi*np.sin(np.pi*angles/180), dtype=float)
    y+=org
    return np.c_[x.T, y.T, np.full((20,1),labelIn)]


a_origin = np.random.randint(-5,20)
b_origin = np.random.randint(5,20)
r_define = 5 * np.random.random_sample((1, 20))



XYa = constructXY(a_origin, r_define,-1)
XYb = constructXY(b_origin, r_define,1)
XY  = np.append(XYa, XYb, axis=0)
XY  = pd.DataFrame({'x': XY[:, 0],
                    'y': XY[:, 1],
                    'col': XY[:, 2]})


pla = PLA.PLAPercep(XY)
pla.PLA()