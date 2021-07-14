# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 15:02:29 2021

@author: tinui
"""
import izhikevich_cells as izh

class chatterCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        self.celltype = 'Chattering' # Regular spiking
        self.C = 50
        self.vr = -60
        self.vt = -40
        self.k = 1.5
        self.a = 0.03
        self.b = 1
        self.c = -40
        self.d = 150
        self.vpeak = 25
        self.stimVal = stimVal
        
    def __repr__(self):
        super().__repr__()
    
    def simulate(self):
        super().simulate()

myCell = chatterCell(4000)
myCell.simulate()

if __name__=='__main__':
    if True:
        izh.plotMyData(myCell)
