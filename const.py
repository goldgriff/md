# -*- coding: utf-8 -*-

import scipy.constants 
import math

#1モル当たりの質量（kg）
UNITM = (1.6605e-27)*scipy.constants.Avogadro

#分子の数
NSP = 108
#ε/ボルツマン定数（温度の単位）
EPS = 119.8
#J/MOL の　何か
EPSIL = EPS*scipy.constants.Boltzmann*scipy.constants.Avogadro
#シグマ、長さの単位(m)
SIGMA = 0.3405**(-9)
#原子量
TMASS = 39.9
#上のキログラム単位
GMASS = TMASS*0.001
#dt(ps)
DT = 0.01
#s単位
DTSECD = DT*10**(-12)
#ステップ数
NSTEP = 10


#直径1シグマの球の体積*Avogadro(m**3/mol)
VO = (4/3.0*scipy.constants.pi)*(SIGMA/2)**3*scipy.constants.Avogadro
#
AFCC = math.sqrt(2)*2**(1/6.0)*SIGMA
#FCC CLOSE PACKING VOLUME
VFCC = (AFCC*3/4.0)*scipy.constants.Avogadro
#直方体(m**3/mol)
VS = SIGMA**3*scipy.constants.Avogadro


#使う体積
VOLUME = VS/0.75
#体積/長方形
VSIGMA = VOLUME/VS
#密度(sigma**-3)
RHO = 1.0/VSIGMA


#temperture
TEMPX = 1.30
#ware
TEMPXD = TEMPX/EPS


#not-restart
RSTART = False
#non-temp scaling
TSCALE = False
#non-save x and vx
NLSAVE = True


#面心立方構造の単位格子を用意し、xyzの方向にnfcc個重ねる
NFCC = (NSP/4.0)**(1.0/3.0)+0.001
#格子定数 in units of cell width
A = 2.0/NFCC
#cellsize
CELLSZ = (VOLUME/scipy.constants.Avogadro*NSP)**(1.0/3.0)
#half cell size
HCELL = 0.5*CELLSZ
#rのunit
RUNIT = HCELL
#sigma の d単位
SIGMAD = SIGMA/RUNIT
#密度
DENSE = NSP/CELLSZ
#dense の　d単位
DENSED = float(NSP)/CELLSZ**3*RUNIT**3
#時間の単位(rのunit)
TIMEO = RUNIT*math.sqrt(GMASS/EPSIL)
#時間の単位(lj)
TIMELJ = TIMEO/RUNIT*SIGMA
#dt の　TIMEO単位
DTD = DTSECD/TIMEO


#0.5では
EKMASS = 0.5*GMASS*(RUNIT/TIMEO)**2/EPSIL
#
EPS12 = 4.0*SIGMAD**12
#
EPS6 = 4.0*SIGMAD**6

##correction term per a particle##
#
ECRR = 4.*scipy.constants.pi*DENSED*(EPS12/9.-EPS6/3.)
#
VIRCRR = 4.*scipy.constants.pi*DENSED*(4.*EPS12/3.-2*EPS6)/6.


#
HSUM = 0.
#
H2SUM = 0.
#
EKSUM = 0.
#
EK2SUM = 0.
#
EPSUM = 0.
#
EKPSUM = 0.
#
VIRSUM = 0.
#
VIR2SUM = 0.
#
SUM = 0.
