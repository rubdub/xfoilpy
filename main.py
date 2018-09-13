# Python interface for automating Xfoil operation
# Ruben D'Sa 9-13-18


import subprocess as sp
import os
import shutil
import sys
import string
import time

# Path for Xfoil in OSX
path_xfoil = '/Applications/Xfoil.app/Contents/Resources/xfoil'

def xfoil(name, Re, alphastart, alphaend, alphaiter):
    def Cmd(cmd):
        ps.stdin.write(cmd+'\n')
    try:
        os.remove(name+'.log')
    except :
        pass
    
    ps = sp.Popen([path_xfoil] ,stdin=sp.PIPE,stdout=sp.PIPE)
    # ps.stderr.close()
    ps.wait(10)
    # Load foil .dat
    Cmd('load '+name)
    print("some")
    Cmd('OPER')
    Cmd('visc '+str(Re))
    Cmd('PACC')
    Cmd(name+'.log')  # output file
    Cmd(' ')          # no dump file
    Cmd('aseq'+str(alphastart))
    Cmd(str(alphaend))
    Cmd(str(alphaiter))
    Cmd(' ')     # escape OPER
    Cmd('quit')  # exit
    


xfoil('MH49_-10copy.dat', 100000, 0, 10, 1)


