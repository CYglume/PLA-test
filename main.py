import PLA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

trainDT_A = pd.DataFrame({'x': random.sample(range(-20,4), 10), 
                         'y': random.sample(range(-20,4), 10),
                         'col': np.repeat(-1,10)})
trainDT_B = pd.DataFrame({'x': random.sample(range(-4,20), 10), 
                         'y': random.sample(range(-4,20), 10),
                         'col': np.repeat(1,10)})
trainDT = pd.concat([trainDT_A, trainDT_B], axis=0)
trainDT.reset_index(inplace=True, drop=True)


pla = PLA.PLAPercep(trainDT)
pla.PLA()