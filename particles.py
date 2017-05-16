# -*- coding: utf-8 -*-
import numpy as np
import const

class Particles:
    def __init__(self,x=None,v=None,dx=None):
        if x is None:
            self._x = self.initial_position()
            self._v = self.initial_velosity()
            self._dx = 0
            self.is_first = 1
        else:
            self._x = x
            self._v = v
            self._dx = dx
            self.is_first = 0

    
    def initial_position(self):
        ux = np.array([[0.5*const.A,0.,0.5*const.A],[0.5*const.A,0.5*const.A,0.],[0.,0.5*const.A,0.5*const.A]])
        #格子を生成
        indices = const.A * np.transpose(np.mgrid[:const.NFCC,:const.NFCC,:const.NFCC]).reshape(-1,3)
        return np.r_[indices,indices+ux[0],indices+ux[1],indices+ux[2]]
			

    def initial_velosity(self):
		pass

    @property
    def x(self):
        return self._x
        
    @property
    def kinetic_energy(self):
         return 0.5 * const.EKMASS * np.sum(self._v**2)

    def verlet(self,forces):
        if is_first:
            is_first = 0
            self._dx = self._v*const.DTD+0.5*forces*const.DTD**2
            self._x = self._x + self._dx
        else:
            dx_f = self._dx+force+const.DTD**2
            self._x = self._x + dx_f
            self._v = (self._dx + dx_f)/(2.+const.DFD)
            self._dx = dx_f

        # x mast be in the basic cell
        self._x = np.array([np.mod(i+1,2) if np.abs(i) else i for position in self._x for i in position]).reshape(len(self._x),3)
        
     
