# -*- coding: utf-8 -*-
import math
import numpy as np
import pdb
import const

class Kinetic:
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
        self._dx_p = None

    
    def initial_position(self):
        delta = 0.1*const.A/math.sqrt(6)
        ux = np.array([[0.5*const.A,0.,0.5*const.A],[0.5*const.A,0.5*const.A,0.],[0.,0.5*const.A,0.5*const.A]])
        #格子を生成
        indices = const.A * np.transpose(np.mgrid[:(const.NFCC),:(const.NFCC),:(const.NFCC)]).reshape(-1,3)
        unrandomed_position = np.r_[indices,indices+ux[0],indices+ux[1],indices+ux[2]]
        unbasiced_position  = unrandomed_position + delta*(2.*np.random.rand(len(unrandomed_position),3)-1)
        # x must be in the basic cell
        tmp = self.basic(unbasiced_position)
        while 1:
            if (np.abs(tmp) < 1).any():
                return tmp
            tmp = self.basic(unbasiced_position)

    #self._xが設定された後呼び出す
    def initial_velosity(self):
        return np.random.rand(len(self._x),3)*2-1

    # def initial_position(self):
    #     return np.array([[0.5,0,0],[-0.5,0,0]])
    #
    # def initial_velosity(self):
    #     return np.array([[0,0,0],[0,0,0]])

    @property
    def x(self):
        return self._x
        
    @property
    def kinetic_energy(self):
         return 0.5 * const.EKMASS * np.sum(self._v**2)

    def verlet(self,forces):
        if self.is_first:
            self.is_first = 0
            self._dx = self._v*const.DTD+0.5*forces*const.DTD**2
            self._x = self._x + self._dx
        else:
            dx_f = self._dx+forces*const.DTD**2
            self._x = self._x + dx_f
            self._v = (self._dx + dx_f)/(2.*const.DTD)
            self._dx_p = self._dx
            self._dx = dx_f

        # x must be in the basic cell
        while (np.abs(self._x) > 1).any():
                self._x = self.basic(self._x)

    def basic(self,position):
        tmp = [p - (int(p)+1)/2*2 if p>1 else ( p-2*((int(p)-1)/2) if p<-1 else p) for r in position for p in r]
        return np.array(tmp).reshape(-1,3)

    def scale_t(self):
        factor = np.sqrt(1.5*const.TEMPXD*const.NSP/self.kinetic_energy)
        if factor > 1.5:
            factor = 1.5
        if factor < 0.6 :
            factor = 0.6

        self._v *= factor
        vmean = np.mean(self._v,axis = 0)
        self._v -= vmean
        self._dx = 2.*const.DTD*self._v - self._dx_p 
