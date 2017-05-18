# -*- coding: utf-8 -*-

import math
import pdb
import warnings
import numpy as np
from scipy.spatial import distance
import const

warnings.filterwarnings('error')

class Potential:
    def __init__(self):
        self.force=[]
        self.potential = 0
        
    def calculate(self,position):
        force=[]
        self.potential = 0
        j = 0
        for i in position:
            # pdb.set_trace()
            others = np.delete(position,j,0)
            diff_i = others - i
            diff_i = diff_i - 2.*np.trunc(diff_i)
            dist = np.sqrt(np.sum(diff_i**2,axis = 1))
            # print dist
            self.potential += np.sum(4 * (const.EPS12 / dist**12 - const.EPS6 / dist**6))
            force_cofficient =np.c_[-4 * (12 * const.EPS12 / dist ** 14 - 6 * const.EPS6 / dist ** 8)]
            force.append(np.sum(diff_i*force_cofficient,axis=0))
            j += 1
            
        self.force = np.array(force)
