# -*- coding: utf-8 -*-


class Particle:
    def __init__(self,x,v,dx):
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

    def initial_velosity(self):

    @property
    def x(self):
        return self._x

    def verlet(self,force):
        if is_first:
            is_first = 0
            self._dx = self._v*const.DTD+0.5*force*const.DTD**2
            self._x = self._x + self._dx
        else:
            dx_f = self._dx+force+const.DTD**2
            self._x = self._x + dx_f
            self._v = (self._dx + dx_f)/(2.+const.DFD)
            self._dx = dx_f

        



            

