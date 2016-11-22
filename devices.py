from __future__ import print_function
from .config import INSTRUMENT, VERBOSE, say
import vlt
from vlt import devices


def loadDevices(to):
    loadMotors(to)
    loadShutters(to)
    loadDetector(to)

def loadDetector(to):    
    pndict = to['pndict']
    pnoc = to['pnoc']

    say("loadding Detector device ...")
    functions = pndict.restrict(
            [("DET.DIT","dit"),
             ("DET.NDIT","ndit"),
             ("DET.POLAR","polar"),
             ("DET.SUBWINS","subwins"),
             ("DET.SUBWIN.COORDINATES", "subwincoord"),
             ("DET.SUBWINi.GEOMETRY","geometry")
            ]            
        ) 
    ## add some functions by hand
    other_functions = vlt.FunctionDict({
                          'type'   :vlt.Function( "DPR.TYPE", dtype=str , format="%s",
                                                  value="DETCAR" ),
                          'catg'   :vlt.Function( "DPR.CATG", dtype=str , format="%s",
                                                  value="TEST" ),
                          'tech'   :vlt.Function( "DPR.TECH", value="IMAGE",
                                                  dtype=str , format="%s"),
                          'imgname':vlt.Function( "OCS.DET.IMGNAME", value="PIONIER_{type}",
                                                  dtype=str , format="%s"),
                          'mode':   vlt.Function( "INS.MODE", dtype=str , format="%s",
                                                  value="ENGINEERING")

                          })
    
    det = devices.Detector(functions+other_functions, proc=pnoc)
    
    say("DET device added -> `det`")    
    to['det'] = det

def loadShutters(to):
    ics = to['ics']
    pnoc = to['pnoc']

    say("loading shuter devices ...")

    shutters = [devices.Shutter(ics.restrict("INS.SHUT%d"%(i)), statusItems=[""], proc=pnoc) for i in range(1,5)]
    say("    INS.SHUT1 device ->  `shut1`")
    say("    INS.SHUT2 device ->  `shut2`")
    say("    INS.SHUT3 device ->  `shut3`")
    say("    INS.SHUT4 device ->  `shut4`")

    to['shut1'], to['shut2'], to['shut3'], to['shut4'] = shutters
    say("  All Shuters -> `shutters`")
    to['shutters'] = devices.Shutters(shutters)

def loadMotors(to):
    ics  = to['ics']
    pnoc = to['pnoc']
    
    say("loading motorized devices ...")

    say("    INS.OPTI1 device ->  `cfou`, `opti1`")
    to['cfou'] = vlt.devices.Motor(ics.restrict("INS.OPTI1"), statusItems=["INS.OPTI1"], proc=pnoc)
    to['opti1'] = to['cfou']

    say("    INS.OPTI2 device ->  `disp`, `opti2`")
    to['disp']  = vlt.devices.Motor(ics.restrict("INS.OPTI2"), statusItems=["INS.OPTI2"], proc=pnoc)
    to['opti2'] = to['disp']

    say("    INS.OPTI3 device ->  `iobcx`, `opti3`")
    to['iobcx']   = vlt.devices.Motor(ics.restrict("INS.OPTI3"), statusItems=["INS.OPTI3"], proc=pnoc)
    to['opti3'] = to['iobcx']

    say("    INS.OPTI4 device ->  `iobcx`, `opti4`")
    to['iobcy']   = vlt.devices.Motor(ics.restrict("INS.OPTI4"), statusItems=["INS.OPTI4"], proc=pnoc)
    to['opti4'] = to['iobcy']

def loadLamp(to):
    ics  = to['ics']
    


