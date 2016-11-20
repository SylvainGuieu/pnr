from __future__ import print_function
from .config import INSTRUMENT, VERBOSE, say
from vlt import devices

def loadDetector(to):    
    pndict = to['pndict']
    
    functions = pndict.restrict(
            [("DET.DIT","dit"),
             ("DET.NDIT","ndit"),
             ("DET.POLAR","polar"),
             ("DET.SUBWINS","subwins"),
             ("DET.SUBWIN.COORINATES","subwincoord"),
             ("DET.SUBWINi.GEOMETRY","geometry")
            ]            
        ) 
    ## add some functions by hand

    
    det = devices.Detector(
        
        
        )
    
