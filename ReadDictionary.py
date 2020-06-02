import numpy as np

units = np.load('unitsDictionary.npy').item()

for stat,val in units.items():
    print(stat,val[85])
