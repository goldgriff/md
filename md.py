# -*- coding: utf-8 -*-

import math
import const
import numpy as np
import pdb
import csv
import kinetic
import potential

if __name__ == '__main__':
    potent = potential.Potential()
    kinet = kinetic.Kinetic()
    fs = []
    for i in range(const.NSTEP):
        print i
        #pdb.set_trace()
        potent.calculate(kinet.x)
        kinet.verlet(potent.force)
        #if i != 0 and i % const.NTSCALE == 0:
            #kinet.scale_t
        fs.append([potent.potential,kinet.kinetic_energy])
    with open('ene.data','w') as f:
        writer = csv.writer(f,lineterminator='\n')
        writer.writerow(['potential','kinetic'])
        for i in fs:
            writer.writerow(i)
                
